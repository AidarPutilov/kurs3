from pathlib import Path
import json


def load_json(path: Path) -> list[dict]:
    """ Загрузка данных JSON из файла """
    with open(path, "r", encoding="UTF-8") as file:
        return json.load(file)
