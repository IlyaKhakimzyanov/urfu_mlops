import sys
from pathlib import Path
import pandas as pd
from sklearn import svm
import pickle

# Взятие рандома из .sh
if len(sys.argv) > 1:
    random_id = int(sys.argv[1])
else:
    random_id = 123

# Расположение
base_path = Path(__file__).parent
train_folder_name = 'train'
train_folder_path = base_path / train_folder_name
model_folder_path = base_path / 'models'

# Чтение
X_train = pd.read_csv(train_folder_path / 'X_train.csv')
y_train = pd.read_csv(train_folder_path / 'y_train.csv').iloc[:, 0]

# Обучение
clf1 = svm.SVC(kernel='linear', C=1, random_state=random_id)
clf1.fit(X_train, y_train)

#
model_folder_path.mkdir(exist_ok=True)

pkl_filename = "SVC_model.pkl"
with open(model_folder_path / pkl_filename, 'wb') as file:
    pickle.dump(clf1, file)
