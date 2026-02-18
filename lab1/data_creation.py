import requests
from pathlib import Path
import sys

# Константы
url = "https://assets.datacamp.com/production/repositories/5981/datasets/8582db71ec282f17c504c8eb794d54758fd8d5d8/telecom_churn_clean.csv"
dataset_name = "telecom_churn_clean.csv"
dataset_folder_name = 'back_dataset'


def find_git_root(current_path):
    for p in Path(current_path).parents:
        if (p / '.git').exists():
            return p
    return None


# __file__ - расположение этого файла
project_root = find_git_root(Path(__file__).resolve())
# print(f"Корень найден тут: {project_root}")
# print(Path(__file__))

if project_root is None:
    print("Ошибка: не найден корень git репозитория")
    sys.exit(1)

# Путь к папку датасета, решил пока не в /tmp скидывать, а локально, чтобы самому смотерть его
dataset_folder_path = project_root / dataset_folder_name
dataset_folder_path.mkdir(exist_ok=True)
dataset_path = dataset_folder_path / dataset_name

# Скачивание файла
response = requests.get(url)
response.raise_for_status()

# Сохранение файла
with open(dataset_path, 'wb') as f:
    f.write(response.content)
