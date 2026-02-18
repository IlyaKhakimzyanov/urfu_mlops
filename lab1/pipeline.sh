#!/bin/bash

# надо отдельный наверное файл для проверки библиотек
echo 'Проверка библиотек'
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"
cd ..
source start.sh > /dev/null 2>&1
echo 'Ок!'
echo 'Запуск pipline'

#
source .venv/bin/activate

python lab1/data_creation.py
