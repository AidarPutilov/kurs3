from settings import DATA_FILE_PATH
from src.functions import (load_json,
                           get_executed_operations,
                           get_operation_instances,
                           sort_operations_by_date)


def main():

    # Чтение данных из файла JSON
    operations = load_json(DATA_FILE_PATH)

    # Выборка операций со статусом 'EXECUTED'
    executed_operations = get_executed_operations(operations)

    # Создание экземпляров класса
    operation_instances = get_operation_instances(executed_operations)

    # Сортировка по дате
    sort_operations = sort_operations_by_date(operation_instances)

    # Вывод статусов операций
    [print(op.get_status()) for op in sort_operations[:5]]


if __name__ == '__main__':
    main()
