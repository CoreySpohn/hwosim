"""Deprecated alias of spaceodyssey; migrate imports to that package.

Submodules are aliases in sys.modules, rather than copied implementations or
wrapper modules. This preserves every object, including private names and
mutable registries, and prevents code from executing under two namespaces.
Root exports refer to the same canonical objects. The local _version module
is retained for hatch-vcs; the public API follows spaceodyssey.__all__.
"""

import importlib as _importlib
import sys as _sys
import warnings as _warnings

import spaceodyssey as _spaceodyssey

_warnings.warn(
    "hwosim is deprecated; import spaceodyssey instead. "
    "Removal will occur once no consumer imports hwosim, "
    "and no earlier than spaceodyssey 0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

_SUBMODULES = (
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
    "engines.mc",
    "errors",
    "io",
    "loop",
    "metrics",
    "observe",
    "policy",
    "registry",
    "rng",
    "seams",
    "spec",
    "testing",
    "universe",
    "wiring",
)

for _name in _SUBMODULES:
    _module = _importlib.import_module(f"spaceodyssey.{_name}")
    _sys.modules[f"{__name__}.{_name}"] = _module
    if "." not in _name:
        globals()[_name] = _module

# Apply exports last: build and observe are functions in the canonical root API.
__all__ = _spaceodyssey.__all__
for _name in __all__:
    globals()[_name] = getattr(_spaceodyssey, _name)

del _name, _module
