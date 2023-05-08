#!/usr/bin/env bash

set -euo pipefail

clean() {
  # Remove build artifacts and temporary files
  rm -rf {build,dist,__pycache__,*.egg-info,**/*.egg-info,*.pyc,**/*.pyc,reports} 2>/dev/null || true
}

qa() {
  # Run static analysis tools
  if command -v flake8 >/dev/null 2>&1; then
    flake8 .
  fi

  python run_pylint.py
}

package() {
  python -m zipfile -c .\builds\AutoGPT_zapier.zip  src\AutoGPT_zapier
  # copy .\builds\AutoGPT_zapier.zip %GPT_HOME%\plugins
  python -m autogpt --debug
  exit /b 0

}

unittest() {
  python -m unittest src/AutoGPT_zapier/zapier_test.py -v
}

style() {
  # Format code
  isort .
  black --exclude=".*/*(dist|venv|.venv|test-results)/*.*" .
}

case "$1" in
  clean)
    echo Removing build artifacts and temporary files...
    clean
    ;;
  qa)
    echo Running static analysis tools...
    qa
    ;;
  style)
    echo Running code formatters...
    style
    ;;
  package)
    echo Building Package...
    package
    ;;
  unittest)
    echo Running unit tests...
    unittest
    ;;
  *)
    echo "Usage: $0 [clean|qa|style|package|unittest]"
    exit 1
    ;;
esac

printf 'Done!\n\n'
exit 0
