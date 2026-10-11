"""Compatibility guarantees for the deprecated package namespace."""

import importlib
import inspect
import os
import subprocess
import sys
import warnings
from pathlib import Path

import pytest
import spaceodyssey

MODULES = (
    "account",
    "aliases",
    "belief",
    "build",
    "certify",
    "context",
    "contracts",
    "data",
    "dist",
    "engines",
    "engines.analytic",
    "engines.mc",
    "errors",
    "io",
    "loop",
    "metrics",
    "observe",
    "policy",
    "registry",
    "reporting",
    "rng",
    "seams",
    "spec",
    "testing",
    "universe",
    "wiring",
)


@pytest.fixture
def alias():
    """Import the alias without leaking its expected warning into other tests."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        return importlib.import_module("hwosim")


@pytest.mark.parametrize("name", spaceodyssey.__all__)
def test_root_exports_are_identical(alias, name):
    """Every root export refers to the canonical object."""
    assert getattr(alias, name) is getattr(spaceodyssey, name)


@pytest.mark.parametrize("name", MODULES)
def test_submodules_are_identical(alias, name):
    """Modules, public classes, functions, and private state are shared."""
    old = importlib.import_module(f"hwosim.{name}")
    new = importlib.import_module(f"spaceodyssey.{name}")
    assert old is new
    for attr, value in vars(new).items():
        if not attr.startswith("_") or inspect.isclass(value):
            assert getattr(old, attr) is value


@pytest.mark.parametrize(
    "first_import",
    [
        "import hwosim",
        "import spaceodyssey",
        "import spaceodyssey.engines.analytic",
    ],
)
@pytest.mark.parametrize(
    "analytic_import",
    ["import hwosim.engines.analytic", "from hwosim.engines import analytic"],
)
@pytest.mark.parametrize("lookup_namespace", ["hwosim", "spaceodyssey"])
@pytest.mark.parametrize("lookup_order", ["before", "after", "both"])
def test_analytic_import_orders(
    first_import, analytic_import, lookup_namespace, lookup_order
):
    """Fresh imports and lazy lookups share one integrate engine registration."""
    lookup = (
        f'import {lookup_namespace}; {lookup_namespace}.engines.get_engine("integrate")'
    )
    statements = [first_import]
    if lookup_order in ("before", "both"):
        statements.append(lookup)
    statements.append(analytic_import)
    if lookup_order in ("after", "both"):
        statements.append(lookup)
    statements.extend(
        [
            "import sys",
            "import hwosim.engines.analytic",
            "import spaceodyssey.engines.analytic",
            'old = sys.modules["hwosim.engines.analytic"]',
            'new = sys.modules["spaceodyssey.engines.analytic"]',
            "assert old is new",
            "assert hwosim.engines is spaceodyssey.engines",
            'assert spaceodyssey.engines.get_engine("integrate") is new.run_integrate',
            'assert hwosim.engines.get_engine("integrate") is new.run_integrate',
            'assert spaceodyssey.engines.ENGINES["integrate"] is old.run_integrate',
        ]
    )
    result = subprocess.run(
        [sys.executable, "-c", "\n".join(statements)],
        env=os.environ,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_fresh_import_warns_once_at_importer():
    """A fresh import warns once and cached or submodule imports stay quiet."""
    saved = {
        name: module
        for name, module in sys.modules.copy().items()
        if name == "hwosim" or name.startswith("hwosim.")
    }
    for name in saved:
        del sys.modules[name]
    try:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always", DeprecationWarning)
            import hwosim

            importlib.import_module("hwosim")
            importlib.import_module("hwosim.certify")
        deprecations = [w for w in caught if w.category is DeprecationWarning]
        assert len(deprecations) == 1
        assert "spaceodyssey" in str(deprecations[0].message)
        assert deprecations[0].filename == __file__
        assert hwosim.SnrThreshold is spaceodyssey.SnrThreshold
    finally:
        for name in tuple(sys.modules):
            if name == "hwosim" or name.startswith("hwosim."):
                del sys.modules[name]
        sys.modules.update(saved)


def test_registration_is_shared(alias, monkeypatch):
    """A registration through the old name is visible through the new name."""
    assert alias.REGISTRY is spaceodyssey.REGISTRY
    seam = "certification"
    monkeypatch.setitem(
        spaceodyssey.REGISTRY._impls,
        seam,
        dict(spaceodyssey.REGISTRY._impls[seam]),
    )

    @alias.register(seam, "alias-test", alias.SeamInfo(operators={"sample"}))
    class Certificate:
        """A temporary implementation registered through the alias."""

    assert spaceodyssey.REGISTRY.get(seam, "alias-test").cls is Certificate


@pytest.mark.parametrize(
    "qualname", ["hwosim.SnrThreshold", "hwosim.certify.SnrThreshold"]
)
def test_historical_contract_resolves(alias, qualname):
    """Stored historical qualified names resolve to the canonical class."""
    contracts = importlib.import_module("spaceodyssey.contracts")
    assert contracts.resolve_contract(qualname) is spaceodyssey.SnrThreshold


def test_alias_source_is_this_checkout(alias):
    """Tests exercise the local shim rather than an installed hwosim copy."""
    root = Path(__file__).resolve().parents[1]
    assert Path(alias.__file__).resolve() == root / "src/hwosim/__init__.py"
