from toolkit.errors import WrongSymbolError


def tokenize(expr):
	# Получаем на вход выражение типа string
	tokens = []
	i = 0
	n = len(expr)

	# Пробегаемся по каждому символу в выражении и проверяем его
	while i < n:
		# Встретили пробел -> пошли дальше
		if expr[i].isspace():
			i+=1
			continue
		# Встретили цифру или точку -> ищем момент, когда число заканчивается и добавляем его в tokens
		if expr[i].isdigit() or expr[i] == '.':
			start = i
			while i < n and (expr[i].isdigit() or expr[i] == '.'):
				i+=1
			tokens.append(('NUMBER', expr[start:i]))
			continue
		# Встретили знак -> добавляем в tokens
		if expr[i] in ('+', '-', '/', '*'):
			# Проверка на унарный знак: если предыдущий токен - оператор, или если это первый токен в выражении, тогда перед нами унарный оператор 
			if expr[i] in ('+', '-') and (len(tokens) == 0 or tokens[-1][0] == 'OPERATOR'):
					tokens.append(('UOPERATOR', expr[i]))
					i+=1
					continue
			# В противном случае - это обычный оператор
			tokens.append(('OPERATOR', expr[i]))
			i+=1
			continue
		# Если символ - не знак, и не число, тогда вызываем ошибку
		raise WrongSymbolError(expr[i])
	return tokens