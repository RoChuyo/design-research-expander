#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO_DIR/skill/design-research-expander"
DST="${CODEX_HOME:-$HOME/.codex}/skills/design-research-expander"

mkdir -p "$(dirname "$DST")"
rm -rf "$DST"
cp -R "$SRC" "$DST"

echo "已安装到：$DST"
echo '请重启 Codex 或新开线程，然后使用：$design-research-expander'
