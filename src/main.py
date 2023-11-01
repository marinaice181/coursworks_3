from src.utils import load_operations, get_last_five_operations
from src.oper import Operation

# Список всех операций
operations_list = load_operations()


# 2 Ограничить последними 5 операциями(EXECUTED)
last_five_operations = get_last_five_operations(operations_list)


# Генерация вывод данных
for element in last_five_operations:
    operation = Operation(element)
    print(f"""\n{operation.date()} {operation.description()} 
{operation.hide_number(operation.account_from())} -> {operation.hide_number(operation.account_to())}
{operation.amount()}""")
