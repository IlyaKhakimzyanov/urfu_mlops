#!/bin/bash

# rand id
random_id=${1:-123}

# надо отдельный наверное файл для проверки библиотек
echo 'Проверка библиотек'
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"
cd ..
source start.sh > /dev/null 2>&1
echo 'Ок!'
echo "Запуск $0"
echo "rand_id = $random_id"

#
source .venv/bin/activate

python lab1/data_creation.py "$random_id"
python lab1/data_preprocessing.py
python lab1/model_preparation.py "$random_id"
python lab1/model_testing.py
