#!/bin/bash

# надо отдельный наверное файл для проверки библиотек
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"
cd ..
source start.sh > /dev/null 2>&1

#
source .venv/bin/activate
