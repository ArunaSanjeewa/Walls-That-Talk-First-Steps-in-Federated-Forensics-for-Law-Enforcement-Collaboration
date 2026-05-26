from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


PROJECT_NAME = "lea-ids-hfl"
DEFAULT_RAW_DIR = Path("data/raw")
DEFAULT_PROCESSED_PATH = Path("data/processed/cicids_clean.parquet")
DEFAULT_PARTITIONS_DIR = Path("data/partitions")
DEFAULT_SHARED_DIR = Path("shared")
DEFAULT_SCALER_PATH = DEFAULT_SHARED_DIR / "preprocessing" / "scaler.json"


@dataclass(frozen=True)
class lea:
    """Simulated LEA-network site using a stable `lea_*` identifier."""

    lea_id: str
    region: str
    preferred_attack_groups: tuple[str, ...]


leaS: tuple[lea, ...] = (
    lea("lea_eu_01", "region_eu", ("BENIGN", "DOS")),
    lea("lea_eu_02", "region_eu", ("BENIGN", "BRUTE_FORCE", "WEB")),
    lea("lea_eu_03", "region_eu", ("BENIGN", "PORTSCAN")),
    lea("lea_na_01", "region_na", ("BENIGN", "DDOS")),
    lea("lea_na_02", "region_na", ("BENIGN", "BOTNET", "INFILTRATION")),
    lea(
        "lea_na_03",
        "region_na",
        (
            "BENIGN",
            "DOS",
            "BRUTE_FORCE",
            "WEB",
            "PORTSCAN",
            "DDOS",
            "BOTNET",
            "INFILTRATION",
            "HEARTBLEED",
            "OTHER_ATTACK",
        ),
    ),
)

REGIONS: tuple[str, ...] = ("region_eu", "region_na")


def leas_by_region(region: str) -> list[lea]:
    leas = [lea for lea in leaS if lea.region == region]
    if not leas:
        raise ValueError(f"Unknown region: {region}")
    return leas


def parse_regions(value: str | None) -> list[str]:
    if not value:
        return list(REGIONS)
    regions = [region.strip() for region in value.split(",") if region.strip()]
    unknown = sorted(set(regions) - set(REGIONS))
    if unknown:
        raise ValueError(f"Unknown regions: {', '.join(unknown)}")
    return regions


def partition_dir(lea_id: str, partitions_dir: Path = DEFAULT_PARTITIONS_DIR) -> Path:
    return partitions_dir / lea_id


def region_checkpoint(region: str, round_number: int, shared_dir: Path = DEFAULT_SHARED_DIR) -> Path:
    return shared_dir / "checkpoints" / region / f"round_{round_number}.pt"


def global_checkpoint(round_number: int, shared_dir: Path = DEFAULT_SHARED_DIR) -> Path:
    return shared_dir / "checkpoints" / "global" / f"round_{round_number}.pt"
