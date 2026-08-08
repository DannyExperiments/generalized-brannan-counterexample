#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO_ROOT=$(dirname -- "$SCRIPT_DIR")
cd "$REPO_ROOT"

python3 scripts/verify_repository.py

if command -v lake >/dev/null 2>&1; then
  (cd formalization/lean && lake build)
fi
