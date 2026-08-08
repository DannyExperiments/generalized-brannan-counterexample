#!/usr/bin/env sh
set -eu

python3 scripts/verify_repository.py

if command -v lake >/dev/null 2>&1; then
  (cd formalization/lean && lake build)
fi
