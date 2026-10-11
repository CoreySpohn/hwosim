hwosim (deprecated)
===================

hwosim is a deprecated alias of
`spaceodyssey <https://github.com/CoreySpohn/spaceodyssey>`_. The campaign core
and its documentation now live there. Replace ``import hwosim`` with
``import spaceodyssey`` and ``hwosim.*`` imports with ``spaceodyssey.*``.

The alias shares classes, functions, modules, and registries with spaceodyssey.
Importing hwosim emits a ``DeprecationWarning``. Previously stored ``hwosim.*``
qualified names continue to resolve through spaceodyssey.

hwosim will be removed once no consumer imports it, and no earlier than
spaceodyssey 0.3.0.
