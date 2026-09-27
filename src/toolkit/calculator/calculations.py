from toolkit.errors import DivisionByZeroError

from .validation import validation

# Приоритет операторов: чем выше число, тем раньше выполняется операция
OPERATORS_PRIORITY = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}


# True, если у текущего оператора приоритет выше, чем у предыдущего.
def is_current_operator_higher_priority(prev: str, current: str) -> bool:
    return OPERATORS_PRIORITY[prev] < OPERATORS_PRIORITY[current]


# Функция вычисления между двумя данными числами и оператором. При делении на 0 вызываем ошибку.
def calculate_two_nums(first_num: float, operator: str, second_num: float) -> float:
    if operator == "+":
        return first_num + second_num
    if operator == "-":
        return first_num - second_num
    if operator == "*":
        return first_num * second_num
    if operator == "/":
        if second_num == 0:
            raise DivisionByZeroError()
        return first_num / second_num


# Удаляем последние 2 числа из стека чисел, последний оператор из стека операторов и передаем эти данные для вычисления. Далее это будет последним элементом в стеке чисел.
def cut_top(nums_stack: list, operators_stack: list) -> None:
    last_num = nums_stack.pop()
    prev_last_num = nums_stack.pop()
    last_operator = operators_stack.pop()
    nums_stack.append(calculate_two_nums(prev_last_num, last_operator, last_num))


# Если в числе найдена точка, то ставим float, чтобы в дальнейшем все выражение было float. Иначе - int.
def parse_number(value: str) -> float | int:
    return float(value) if "." in value else int(value)


# Создаем стек чисел и стек операторов. Добавляем туда числа и операторы. И выполняем вычисления между последними элементами.
def calculate(expr):
    nums_stack = []
    operators_stack = []
    tokens = validation(expr)

    i = 0
    while i < len(tokens):
        token = tokens[i]

        # Число просто кладем в стек чисел
        if token[0] == "NUMBER":
            nums_stack.append(parse_number(token[1]))

        elif token[0] == "OPERATOR":
            # Пока на вершине стека операторов лежит оператор с таким же или выше приоритетом предыдущего, выполняем вычесление между последними числами. Затем добавляем новый оператор в стек.
            while operators_stack and not is_current_operator_higher_priority(
                operators_stack[-1], token[1]
            ):
                cut_top(nums_stack, operators_stack)
            operators_stack.append(token[1])

        elif token[0] == "UOPERATOR":
            # Унарный знак сразу добавляем к следующему числу и кладем как одно число
            next_num = tokens[i + 1][1]
            num_with_uoperator = token[1] + next_num
            nums_stack.append(parse_number(num_with_uoperator))
            i += 1  # пропускаем токен числа, он уже обработан выше

        i += 1

    # Когда токены кончились - выполняем последнее вычисление между тем, что осталось в стеке операторов
    while operators_stack:
        cut_top(nums_stack, operators_stack)

    return nums_stack[0]