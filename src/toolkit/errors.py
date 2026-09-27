# Обработка ошибок. Все пользовательские ошибки наследуются от CalculatorError, чтобы CLI мог ловить их одним except и завершать программу с кодом 2.

# Базовый класс для всех ошибок
class CalculatorError (Exception):
	pass

# Пустое выражение
class EmptyExpressionError (CalculatorError):
	def __init__(self):
		super().__init__('Выражение не может быть пустым')

# Число начинается с точки 
class DotInTheBegginingError (CalculatorError):
	def __init__(self, value):
		super().__init__(f'Число не может начинаться с точки: {value}')

# Число заканчивается точкой
class DotAtTheEndError (CalculatorError):
	def __init__(self, value):
		super().__init__(f'Число не может заканчиваться точкой: {value}')

# Более одной точки в числе
class ManyDotsError (CalculatorError):
	def __init__(self, value):
		super().__init__(f'В числе не может быть более одной точки: {value}')

# Выражение начинается с оператора (кроме бинарного)
class OperatorInTheBegginingError (CalculatorError):
	def __init__(self, value):
		super().__init__(f"Выражение не может начинаться с оператора: {value}")

# Выражение заканчивается оператором
class OperatorAtTheEndError (CalculatorError):
	def __init__(self, value):
		super().__init__(f"Выражение не может заканчиваться оператором: {value}")

# Два или более оператора подряд
class ManyOperatorsError (CalculatorError):
	def __init__(self, value):
		super().__init__(f"Операторы не могут идти подряд: {value}")

# Два и более числа подряд
class ManyNumbersError (CalculatorError):
	def __init__(self, value):
		super().__init__(f'Числа не могут идти подряд: {value}')

# Недопустимый символ
class WrongSymbolError (CalculatorError):
	def __init__(self, value):
		super().__init__(f'Недопустимый символ: {value}')

# Деление на ноль
class DivisionByZeroError (CalculatorError):
	def __init__(self):
		super().__init__('Деление на ноль запрещено')

# Неизвестная единица измерения
class UnknownUnitError(CalculatorError):
    def __init__(self, value):
        super().__init__(f"Неизвестная единица измерения: {value}")

# Несовместимые единицы измерения
class IncompatibleUnitsError(CalculatorError):
    def __init__(self, value):
        super().__init__(f"Несовместимые единицы измерения: {value}")

# Температура не может быть ниже абсолютного нуля
class BelowAbsoluteZeroError(CalculatorError):
    def __init__(self, value):
        super().__init__(f"Температура ниже абсолютного нуля: {value}")