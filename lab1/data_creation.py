# Система
import requests
from pathlib import Path
import sys
# ИИ
import pandas as pd
from sklearn.model_selection import train_test_split

# Взятие рандома из .sh
if len(sys.argv) > 1:
    random_id = int(sys.argv[1])
else:
    random_id = 123

# Константы
url = "https://assets.datacamp.com/production/repositories/5981/datasets/8582db71ec282f17c504c8eb794d54758fd8d5d8/telecom_churn_clean.csv"
dataset_name = "telecom_churn_clean.csv"
dataset_folder_name = 'back_dataset'
train_folder_name = 'train'
test_folder_name = 'test'


def find_git_root(current_path):
    for p in Path(current_path).parents:
        if (p / '.git').exists():
            return p
    return None


# __file__ - расположение этого файла
project_root = find_git_root(Path(__file__).resolve())
base_path = Path(__file__).parent
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

# Разделение датасета
df = pd.read_csv(dataset_path)
df = df.drop(df.columns[0], axis=1)
X = df.drop(['churn'], axis=1)
y = df['churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=random_id,
    stratify=y
)

# Формируем пути
train_folder_path = base_path / train_folder_name
test_folder_path = base_path / test_folder_name

# Создаем папки
train_folder_path.mkdir(exist_ok=True)
test_folder_path.mkdir(exist_ok=True)

# Сохраняем (перезапись произойдет автоматически)
X_train.to_csv(train_folder_path / 'X_train.csv', index=False)
y_train.to_csv(train_folder_path / 'y_train.csv', index=False)

X_test.to_csv(test_folder_path / 'X_test.csv', index=False)
y_test.to_csv(test_folder_path / 'y_test.csv', index=False)
