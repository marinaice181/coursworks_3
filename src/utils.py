import json
import os



path_data = os.path.abspath("../data/")
"""
путь в переменную
"""
path_oper= os.path.join(path_data, "operations.json")


def load_operations():
    """
    Загрузка файла и формируется список операций (json)
    """
    with open(path_oper, "r", encoding='utf8') as file:
        oper_list = json.load(file)
        return oper_list


def get_last_five_operations(oper_list):
    """
    Отсортировать последние 5 по дате выполненных клиентом операций
    """
    oper_list_clean = [opr for opr in oper_list if opr != {} and opr["state"] == "EXECUTED"]
    oper_list_clean.sort(key=lambda dictionary: dictionary["date"], reverse=True)
    """
    1 Ограничить последними 5 операциями
    """
    last_five_oper = oper_list_clean[0:5]
    return last_five_oper