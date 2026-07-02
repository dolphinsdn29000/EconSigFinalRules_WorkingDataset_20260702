#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="/Volumes/OWC Envoy Pro FX/EconSigFinalRules_WorkingDataset_20260702"
SSH_KEY="${HOME}/.ssh/id_ed25519_github_econsig_20260702"

cd "$PROJECT_ROOT"

if [[ ! -d .git ]]; then
  echo "Not a git repository: $PROJECT_ROOT" >&2
  exit 1
fi

stage_safe_files() {
  git add -u -- \
    '*.py' '*.R' '*.r' '*.Rmd' '*.rmd' '*.qmd' '*.do' '*.sh' '*.sql' \
    '*.md' '*.txt' '*.yaml' '*.yml' '*.json' '*.toml' '*.ini' \
    'requirements.txt' 'pyproject.toml' 'renv.lock' 'DESCRIPTION' \
    'AGENTS.md' '.gitignore'

  find . \
    -path './.git' -prune -o \
    -path './data' -prune -o \
    -path './source_inputs' -prune -o \
    -path './generated_outputs' -prune -o \
    -path './raw' -prune -o \
    -path './raw_data' -prune -o \
    -path './data_raw' -prune -o \
    -path './data_intermediate' -prune -o \
    -path './data_final' -prune -o \
    -path './input' -prune -o \
    -path './inputs' -prune -o \
    -path './outputs' -prune -o \
    -path './output' -prune -o \
    -path './results' -prune -o \
    -path './figures' -prune -o \
    -path './figure' -prune -o \
    -path './plots' -prune -o \
    -path './plot' -prune -o \
    -path './logs' -prune -o \
    -path './log' -prune -o \
    -path './tmp' -prune -o \
    -path './temp' -prune -o \
    -path './cache' -prune -o \
    -type f \( \
      -name '*.py' -o -name '*.R' -o -name '*.r' -o -name '*.Rmd' -o \
      -name '*.rmd' -o -name '*.qmd' -o -name '*.do' -o -name '*.sh' -o \
      -name '*.sql' -o -name '*.md' -o -name '*.txt' -o -name '*.yaml' -o \
      -name '*.yml' -o -name '*.json' -o -name '*.toml' -o -name '*.ini' -o \
      -name 'requirements.txt' -o -name 'pyproject.toml' -o -name 'renv.lock' -o \
      -name 'DESCRIPTION' -o -name 'AGENTS.md' -o -name '.gitignore' \
    \) -print0 | xargs -0 git add --

  git restore --staged -- \
    '.env' '.env.*' '*credential*' '*credentials*' '*secret*' '*token*' \
    '*private_key*' '*id_rsa*' '*id_ed25519*' 2>/dev/null || true
}

while true; do
  stage_safe_files

  if git diff --cached --quiet; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') no code/config/doc changes to sync"
  else
    git status --short
    git commit -m "Code autosync $(date '+%Y-%m-%d %H:%M:%S')"

    if [[ -f "$SSH_KEY" ]]; then
      GIT_SSH_COMMAND="ssh -i ${SSH_KEY} -o IdentitiesOnly=yes" git push origin HEAD
    else
      git push origin HEAD
    fi
  fi

  sleep 60
done
