#!/bin/bash

# надо отдельный наверное файл для проверки библиотек
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"
cd ..
echo 'path is'
pwd

#
source .venv/bin/activate
