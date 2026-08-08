#!/usr/bin/env python3
"""Build the deterministic, public-safe AMR-022-5044 evidence bundle."""

from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release" / "EVIDENCE_BUNDLE.zip"
PREFIX = "AMR-022-5044_PUBLIC_EVIDENCE_V1/"
FIXED_TIME = (2026, 8, 8, 0, 0, 0)

MEMBERS = (
    "README.md",
    "STATUS.md",
    "CITATION.cff",
    "AI_DISCLOSURE.md",
    "PROVENANCE.md",
    "ORIGINAL_PROBLEM.md",
    "CLAIM_SCOPE_AND_LIMITATIONS.md",
    "PRIOR_ART_AND_LIMITATIONS.md",
    "CLAIMS_EVIDENCE_MATRIX.md",
    "REPRODUCIBILITY.md",
    "LICENSE_STATUS.md",
    "proof/PROBLEM_AND_PROOF.md",
    "audits/MATHEMATICAL_AUDIT.md",
    "audits/LITERATURE_PRIORITY_AUDIT.md",
    "evidence/AUDIT_SUMMARY.md",
    "checks/EXPECTED_OUTPUT.txt",
    "checks/verify_counterexample.py",
    "paper/manuscript.tex",
    "paper/manuscript.pdf",
    "paper/references.bib",
    "paper/BUILD.md",
    "paper/BUILD_LOG.txt",
    "paper/PDF_PREFLIGHT.txt",
    "paper/MANUSCRIPT_COMPARISON.md",
    "formalization/README.md",
    "formalization/lean/README.md",
    "formalization/lean/lean-toolchain",
    "formalization/lean/lakefile.toml",
    "formalization/lean/lake-manifest.json",
    "formalization/lean/AMR022.lean",
    "formalization/lean/Axioms.lean",
    "formalization/lean/LEAN_AXIOMS.txt",
    "release/RELEASE_NOTES_DRAFT.md",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    missing = [name for name in MEMBERS if not (ROOT / name).is_file()]
    if missing:
        raise SystemExit("missing bundle members: " + ", ".join(missing))

    payloads = {name: (ROOT / name).read_bytes() for name in MEMBERS}
    ledger = "".join(
        f"{sha256(payloads[name])}  {name}\n" for name in sorted(MEMBERS)
    ).encode("utf-8")
    payloads["BUNDLE_SHA256SUMS.txt"] = ledger

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name in sorted(payloads):
            info = zipfile.ZipInfo(PREFIX + name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, payloads[name])

    print(f"built {OUTPUT.relative_to(ROOT)}")
    print(f"sha256 {sha256(OUTPUT.read_bytes())}")


if __name__ == "__main__":
    main()
