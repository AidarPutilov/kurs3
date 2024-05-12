from pathlib import Path
import json
from src.operation import Operation


def load_json(path: Path) -> list[dict]:
    """ Загрузка данных JSON из файла """
    with open(path, "r", encoding="UTF-8") as file:
        return json.load(file)


def get_executed_operations(operations: list[dict]) -> list[dict]:
    """ Возвращает список операций со статусом EXECUTED """
    return [
        operation
        for operation in operations
        if operation.get('state') == 'EXECUTED'
    ]


def get_operation_instances(operations: list[dict]) -> list[Operation]:
    """ Возвращает экземпляры класса """
    return [
        Operation(
            pk=operation['id'],
            state=operation['state'],
            date_time=operation['date'],
            amount=operation['operationAmount']['amount'],
            currency=operation['operationAmount']['currency']['name'],
            description=operation.get('description'),
            from_=operation.get('from'),
            to=operation.get('to')
        )
        for operation in operations
    ]


def sort_operations_by_date(operations: list[Operation]) -> list[Operation]:
    """ Сортировка по полю date_time в убывающем порядке """
    return sorted(operations, reverse=True)
