from pathlib import Path
import pandas as pd

# Расположения
base_path = Path(__file__).parent
train_folder_name = 'train'
test_folder_name = 'test'
train_folder_path = base_path / train_folder_name
test_folder_path = base_path / test_folder_name

#
X_train = pd.read_csv(train_folder_path / 'X_train')
y_train = pd.read_csv(train_folder_path / 'y_train')
X_test = pd.read_csv(test_folder_path / 'X_test')
y_test = pd.read_csv(test_folder_path / 'y_test')
