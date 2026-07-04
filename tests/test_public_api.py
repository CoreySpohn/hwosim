"""Tests for the public package surface."""

import hwosim


def test_all_names_importable():
    """Every advertised name resolves on the top-level package."""
    for name in hwosim.__all__:
        assert getattr(hwosim, name) is not None


def test_default_registry_entries_available():
    """The in-tree reference implementations are discoverable and usable."""
    for seam, name in (
        ("certification", "snr_threshold"),
        ("context", "always_observable"),
        ("cost", "constant_overheads"),
    ):
        entry = hwosim.REGISTRY.get(seam, name)
        assert entry.available, f"{seam}:{name} unavailable: {entry.reason}"


def test_sample_engine_available():
    """The sampling engine resolves through the public entry point."""
    assert callable(hwosim.get_engine("sample"))
