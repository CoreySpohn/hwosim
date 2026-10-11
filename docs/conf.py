"""Sphinx configuration for the hwosim deprecation page."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as get_version

project = "hwosim"
copyright = "2026, Corey Spohn"
author = "Corey Spohn"
try:
    release = get_version("hwosim")
except PackageNotFoundError:
    release = "unreleased"
version = ".".join(release.split(".")[:2])

extensions = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "en"
html_theme = "alabaster"
master_doc = "index"
html_title = "hwosim - deprecated alias of spaceodyssey"
source_suffix = {".rst": "restructuredtext"}
