"""hwosim: closed-loop mission simulation and yield estimation for direct imaging."""

from hwosim._version import __version__
from hwosim.belief import MissionBelief, TargetBelief
from hwosim.certify import AbstractCertificate, CertificateState, SnrThreshold
from hwosim.data import Observation, SummaryDataset
from hwosim.dist import AbstractPredictive, GaussianSummary
from hwosim.errors import RegistryError, UnsupportedOperator, WiringError
from hwosim.registry import REGISTRY, RegisteredImpl, Registry, SeamInfo, register
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
from hwosim.wiring import WiringFailure, WiringReport

__all__ = [
    "REGISTRY",
    "AbstractCertificate",
    "AbstractPredictive",
    "CertificateState",
    "FidelityConfig",
    "FileRef",
    "GaussianSummary",
    "MissionBelief",
    "MissionSpec",
    "Observation",
    "RegisteredImpl",
    "Registry",
    "RegistryError",
    "SeamChoice",
    "SeamInfo",
    "SeamRef",
    "SnrThreshold",
    "SummaryDataset",
    "TargetBelief",
    "UnsupportedOperator",
    "WiringError",
    "WiringFailure",
    "WiringReport",
    "__version__",
    "config_from_json",
    "content_hash",
    "register",
    "spec_from_json",
    "to_json",
]
