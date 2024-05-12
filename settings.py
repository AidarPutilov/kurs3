from os.path import abspath, join
from pathlib import Path

# Каталог с проектом
ROOT_PATH = Path(__file__).parent

# Файл с данными
DATA_FILE_PATH = ROOT_PATH.joinpath('src', 'data', 'operations.json')

# Количество отображаемых операций
OPERATIONS_COUNT = 5

#print(DATA_FILE_PATH)
