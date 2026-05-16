#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="${1:-design-research-expander}"
VISIBILITY="${2:-public}"
DESCRIPTION="Codex Skill for expanding product design research proposals with Chinese literature/case synthesis, direction exploration, workload estimation, and organized research archives."

if ! command -v gh >/dev/null 2>&1; then
  echo "未找到 GitHub CLI：gh"
  echo "请先运行：brew install gh"
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "GitHub CLI 尚未登录。请先运行：gh auth login"
  echo "建议选择：GitHub.com -> HTTPS -> Login with a web browser"
  exit 1
fi

if [ "$VISIBILITY" != "public" ] && [ "$VISIBILITY" != "private" ]; then
  echo "可见性只能是 public 或 private"
  echo "用法：./发布到GitHub.sh [仓库名] [public|private]"
  exit 1
fi

git status --short

if [ -n "$(git status --short)" ]; then
  echo "检测到未提交改动，正在提交..."
  git add .
  git commit -m "Prepare GitHub release"
fi

if git remote get-url origin >/dev/null 2>&1; then
  echo "已存在 origin：$(git remote get-url origin)"
else
  echo "正在创建 GitHub 仓库：$REPO_NAME ($VISIBILITY)"
  if [ "$VISIBILITY" = "public" ]; then
    gh repo create "$REPO_NAME" --public --source=. --remote=origin --description "$DESCRIPTION"
  else
    gh repo create "$REPO_NAME" --private --source=. --remote=origin --description "$DESCRIPTION"
  fi
fi

echo "正在推送 main 分支..."
git push -u origin main

echo "设置 GitHub topics..."
gh repo edit "$REPO_NAME" \
  --add-topic codex-skill \
  --add-topic product-design \
  --add-topic design-research \
  --add-topic industrial-design \
  --add-topic cmf-design \
  --add-topic research-assistant \
  --add-topic chinese \
  --add-topic literature-review \
  --add-topic case-study \
  --add-topic human-centered-design \
  --add-topic universal-design || true

echo "发布完成："
gh repo view "$REPO_NAME" --web
