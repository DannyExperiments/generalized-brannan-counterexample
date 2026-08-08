#!/usr/bin/env python3
"""Dependency-free verification of the sanitized repository surface."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_ledger() -> None:
    ledger = ROOT / "SHA256SUMS.txt"
    if not ledger.is_file():
        fail("missing SHA256SUMS.txt")
    for number, line in enumerate(ledger.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            expected, relative = line.split("  ", 1)
        except ValueError:
            fail(f"malformed checksum line {number}")
        target = ROOT / relative
        if not target.is_file():
            fail(f"checksum target missing: {relative}")
        if sha256(target) != expected:
            fail(f"checksum mismatch: {relative}")


def verify_required_files() -> None:
    required = [
        "README.md",
        "ORIGINAL_PROBLEM.md",
        "CLAIM_SCOPE_AND_LIMITATIONS.md",
        "PRIOR_ART_AND_LIMITATIONS.md",
        "AI_DISCLOSURE.md",
        "PROVENANCE.md",
        "paper/manuscript.tex",
        "paper/references.bib",
        "checks/verify_counterexample.py",
        "checks/EXPECTED_OUTPUT.txt",
        "proof/PROBLEM_AND_PROOF.md",
        "audits/MATHEMATICAL_AUDIT.md",
        "audits/LITERATURE_PRIORITY_AUDIT.md",
        "scripts/build_evidence_bundle.py",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail(f"required file missing: {relative}")


def verify_scope_markers() -> None:
    manuscript = (ROOT / "paper/manuscript.tex").read_text(encoding="utf-8")
    required = [
        r"\frac{33}{686}",
        r"\frac{20}{343}",
        r"1/98",
        "all-positive",
        "unit-square Brannan conjecture",
        "moderate confidence",
        "Absolute historical priority is not claimed",
    ]
    for marker in required:
        if marker not in manuscript:
            fail(f"manuscript scope marker missing: {marker}")


def verify_privacy() -> None:
    forbidden = [
        re.compile(r"chatgpt\.com/c/", re.I),
        re.compile(r"chatgpt\.com/(share|s|t)/", re.I),
        re.compile("sandbox" + r":/", re.I),
        re.compile(r"/Users/[A-Za-z0-9._-]+/"),
        re.compile(r"\\Users\\[A-Za-z0-9._-]+\\"),
        re.compile("/private" + r"/var/", re.I),
        re.compile("codex" + r"/attachments", re.I),
        re.compile("file" + r"_[0-9a-f]{12,}", re.I),
        re.compile("6a738" + "b62", re.I),
    ]
    suffixes = {
        ".md", ".tex", ".bib", ".py", ".yml", ".yaml", ".txt",
        ".json", ".cff", ".toml", ".sh",
    }
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if ".git" in relative.parts or ".lake" in relative.parts:
            continue
        if not path.is_file() or path.name == "SHA256SUMS.txt" or path.suffix.lower() not in suffixes:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in forbidden:
            if pattern.search(text):
                fail(f"private-data pattern in {relative}: {pattern.pattern}")


def replay_counterexample() -> None:
    result = subprocess.run(
        [sys.executable, "checks/verify_counterexample.py"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    expected = (ROOT / "checks/EXPECTED_OUTPUT.txt").read_text(encoding="utf-8")
    if result.stdout != expected:
        fail("exact verifier output differs from EXPECTED_OUTPUT.txt")


def main() -> None:
    verify_required_files()
    verify_scope_markers()
    verify_privacy()
    replay_counterexample()
    verify_ledger()
    print("REPOSITORY_INTEGRITY=PASS")
    print("SCOPE_MARKERS=PASS")
    print("PRIVATE_DATA_SCAN=PASS")
    print("EXACT_COUNTEREXAMPLE_REPLAY=PASS")


if __name__ == "__main__":
    main()
