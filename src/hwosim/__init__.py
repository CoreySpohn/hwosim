"""hwosim: closed-loop mission simulation and yield estimation for direct imaging.

The package is three thin things plus adapters: a vocabulary (the mission
data model and the seam interfaces), a registry and resolver (named seam
implementations compiled from declarative configuration by ``build``), and
engines (one run callable per outcome operator, all emitting one report
schema). Physics, inference, and policy live in the wider simulation suite
and enter through adapters; if a module here starts accumulating physics, it
is in the wrong package.
"""

from hwosim._version import __version__
from hwosim.account import ConstantOverheads, Ledger
from hwosim.belief import MissionBelief, TargetBelief
from hwosim.build import Mission, ModelStack, TruthStack, build
from hwosim.certify import AbstractCertificate, CertificateState, SnrThreshold
from hwosim.context import AbstractContextProvider, AlwaysObservable
from hwosim.data import Observation, SummaryDataset
from hwosim.dist import AbstractPredictive, GaussianSummary
from hwosim.engines import get_engine, register_engine, run
from hwosim.errors import RegistryError, UnsupportedOperator, WiringError
from hwosim.io import RunManifest, read_manifest, write_run
from hwosim.loop import (
    DETECTION_CERTIFICATE,
    MissionState,
    observe,
    run_mission,
    step,
)
from hwosim.metrics import YieldSummary, summarize
from hwosim.observe import AbstractMeasurement
from hwosim.registry import (
    REGISTRY,
    RegisteredImpl,
    Registry,
    SeamInfo,
    register,
)
from hwosim.rng import Purpose, stream
from hwosim.seams import DATA_PLANE_EDGES, KNOWN_OPERATORS, SEAMS
from hwosim.spec import (
    FidelityConfig,
    FileRef,
    MissionSpec,
    SeamChoice,
    SeamRef,
    config_from_json,
    content_hash,
    spec_from_json,
    to_json,
)
from hwosim.universe import AbstractUniverseSource, FixedUniverse, Universe
from hwosim.wiring import WiringFailure, WiringReport

__all__ = [
    "DATA_PLANE_EDGES",
    "DETECTION_CERTIFICATE",
    "KNOWN_OPERATORS",
    "REGISTRY",
    "SEAMS",
    "AbstractCertificate",
    "AbstractContextProvider",
    "AbstractMeasurement",
    "AbstractPredictive",
    "AbstractUniverseSource",
    "AlwaysObservable",
    "CertificateState",
    "ConstantOverheads",
    "FidelityConfig",
    "FileRef",
    "FixedUniverse",
    "GaussianSummary",
    "Ledger",
    "Mission",
    "MissionBelief",
    "MissionSpec",
    "MissionState",
    "ModelStack",
    "Observation",
    "Purpose",
    "RegisteredImpl",
    "Registry",
    "RegistryError",
    "RunManifest",
    "SeamChoice",
    "SeamInfo",
    "SeamRef",
    "SnrThreshold",
    "SummaryDataset",
    "TargetBelief",
    "TruthStack",
    "Universe",
    "UnsupportedOperator",
    "WiringError",
    "WiringFailure",
    "WiringReport",
    "YieldSummary",
    "__version__",
    "build",
    "config_from_json",
    "content_hash",
    "get_engine",
    "observe",
    "read_manifest",
    "register",
    "register_engine",
    "run",
    "run_mission",
    "spec_from_json",
    "step",
    "stream",
    "summarize",
    "to_json",
    "write_run",
]
