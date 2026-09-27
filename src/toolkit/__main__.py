import sys
from toolkit.calculator import validation
from toolkit.errors import CalculatorError
from toolkit.calculator.calculations import calculate

if __name__ == "__main__":
	if sys.argv[1] == "calc":
		try:
			# is_valid = validation(sys.argv[2])
			calc = calculate(sys.argv[2])
			print(calc)
		except CalculatorError as e:
			print(f'Ошибка: {e}', file=sys.stderr)
			sys.exit(2)
			