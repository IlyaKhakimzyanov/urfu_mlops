from pathlib import Path
import pandas as pd
# from sklearn import svm
import pickle

# Расположение
base_path = Path(__file__).parent
test_folder_name = 'test'
test_folder_path = base_path / test_folder_name
model_folder_path = base_path / 'model'
model_name = 'SVC_model.pkl'

# Загрузка test
X_test = pd.read_csv(test_folder_path / 'X_test.csv')
y_test = pd.read_csv(test_folder_path / 'y_test.csv').iloc[:, 0]

# Загрузка модели
with open(model_folder_path / model_name, 'rb') as file:
    load_model = pickle.load(file)

#
score = load_model.score(X_test, y_test)

print(f'Model test accuracy is: {score:.3f}')
