from pathlib import Path
import pandas as pd
from sklearn import preprocessing

# Расположения
base_path = Path(__file__).parent
train_folder_name = 'train'
test_folder_name = 'test'
train_folder_path = base_path / train_folder_name
test_folder_path = base_path / test_folder_name

#
X_train = pd.read_csv(train_folder_path / 'X_train.csv')
# y_train = pd.read_csv(train_folder_path / 'y_train.csv')
X_test = pd.read_csv(test_folder_path / 'X_test.csv')
# y_test = pd.read_csv(test_folder_path / 'y_test.csv')

#
scaler = preprocessing.StandardScaler().set_output(transform="pandas")
scaler.fit(X_train)

#
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Перезапись данных
X_train_scaled.to_csv(train_folder_path / 'X_train.csv', index=False)
X_test_scaled.to_csv(test_folder_path / 'X_test.csv', index=False)
