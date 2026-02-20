#!/usr/bin/env bash
# sync-repos.sh — Push to both GitHub remotes (github.com + github.dxc.com)
#
# Usage:
#   ./scripts/sync-repos.sh                  # Push current branch to both
#   ./scripts/sync-repos.sh "commit message" # Commit all changes, then push to both

set -euo pipefail

BRANCH=$(git rev-parse --abbrev-ref HEAD)
MSG="${1:-}"

echo "→ Branch: $BRANCH"

# Optional: commit staged + unstaged changes
if [[ -n "$MSG" ]]; then
  echo "→ Committing: $MSG"
  git add -A
  git commit -m "$MSG"
fi

# Push to github.com
echo "→ Pushing to github.com (origin)..."
git push origin "$BRANCH"

# Push to github.dxc.com
echo "→ Pushing to github.dxc.com (dxc)..."
git push dxc "$BRANCH"

echo "✓ Both repos updated."
