# Функция Валидация. Реализована методом посимвольного анализа. Пробегаемся по каждому токену после токенизации и проверяем общее выражение на различные ошибки, например, 2 числа подряд; точка в конце выражения; 2 оператора подряд и другое.

from toolkit.errors import *

from .tokenizer import tokenize


def validation (expr):
	tokens = tokenize(expr)

	# Выражение не может быть пустым
	if len(tokens) == 0:
		raise EmptyExpressionError()

	# Выражение не может начинаться с оператора (но может с бинарного) 
	if tokens[0][0] == 'OPERATOR':
		raise OperatorInTheBegginingError(tokens[0][1])

	# Выражение не может заканчиваться любым оператором 
	if tokens[-1][0] in ('OPERATOR', 'UOPERATOR'):
		raise OperatorAtTheEndError(tokens[-1][1])

	# Пробегаемся по каждому токену
	for i in range(len(tokens)):
		current_data = tokens[i][1]
		current_type = tokens[i][0]

		# В числе не может быть более одной точки
		if current_data.count('.') > 1:
			raise ManyDotsError(current_data)

		# Выражение не может начинаться с точки
		if current_data[0] == '.':
			raise DotInTheBegginingError(current_data)

		# Выражение не может заканчиваться точкой
		if current_data[-1] == '.':
			raise DotAtTheEndError(current_data)
	
		# Сравнение с токеном справа (если он есть) 
		if i < len(tokens) - 1:
			next_type = tokens[i + 1][0]
			next_data = tokens[i + 1][1]

			# 2 числа не могут идти подряд
			if current_type == 'NUMBER' and next_type == 'NUMBER':
				raise ManyNumbersError(f'{current_data}, {next_data}')

			# После любого оператора не может идти еще один оператор, например 2+/2
			if current_type in ('UOPERATOR', 'OPERATOR') and next_type == 'OPERATOR':
				raise ManyOperatorsError(f'{current_data}, {next_data}')
	return tokens
