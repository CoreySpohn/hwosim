<p align="center">
  <a href="https://pypi.org/project/hwosim/"><img src="https://img.shields.io/pypi/v/hwosim.svg?style=flat-square&logo=pypi" alt="PyPI"/></a>
  <a href="https://hwosim.readthedocs.io"><img src="https://readthedocs.org/projects/hwosim/badge/?version=latest&style=flat-square" alt="Documentation Status"/></a>
  <a href="https://github.com/CoreySpohn/hwosim/actions/workflows/tests.yml"><img src="https://img.shields.io/github/actions/workflow/status/CoreySpohn/hwosim/tests.yml?branch=main&style=flat-square&logo=github&label=tests" alt="Tests"/></a>
  <a href="https://github.com/CoreySpohn/hwosim/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="https://github.com/CoreySpohn/hwosim"><img src="https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12-blue.svg?style=flat-square&logo=python" alt="Python Versions"></a>
</p>

---

# hwosim

**hwosim** is a JAX-based toolkit for running end-to-end Habitable Worlds Observatory (HWO) mission simulations. It ties together the full suite of HWO direct imaging simulation tools:

- **[yippy](https://github.com/CoreySpohn/yippy)** — Coronagraph performance modeling
- **[orbix](https://github.com/CoreySpohn/orbix)** — Orbital dynamics and target scheduling
- **[coronagraphoto](https://github.com/CoreySpohn/coronagraphoto)** — Image simulation for coronagraphic observations
- **[coronalyze](https://github.com/CoreySpohn/coronalyze)** — Post-processing and SNR analysis
- All the other ones I need to still write

## Key Features

*   **Mission Simulation**: End-to-end simulation pipelines from target selection through observation and analysis
*   **Yield Estimation**: Detection completeness and exoplanet yield calculations
*   **Integration Orchestration**: Unified interface across the HWO simulation suite
*   **JAX-Native**: Fully JIT-compilable, differentiable, and GPU-accelerated

## Installation

With [uv](https://docs.astral.sh/uv/) (recommended):

```bash
uv pip install hwosim
```

Or with pip:

```bash
pip install hwosim
```

*(Note: You may need to install JAX separately to match your specific hardware acceleration requirements.)*

## Quick Start

```python
import hwosim
```

## Documentation

Full documentation is available at [hwosim.readthedocs.io](https://hwosim.readthedocs.io).
