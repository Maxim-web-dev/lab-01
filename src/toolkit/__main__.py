import sys

from toolkit.calculator.calculations import calculate
from toolkit.converter import convert
from toolkit.errors import CalculatorError


def print_help():
    print("Использование:")
    print('python -m toolkit calc "EXPRESSION"')
    print("python -m toolkit convert VALUE --from UNIT --to UNIT")
    print("python -m toolkit --help")


if __name__ == "__main__":
    if sys.argv[1] == "--help":
        print_help()
        sys.exit(0)

    try:
        if sys.argv[1] == "calc":
            result = calculate(sys.argv[2])
            print(result)

        elif sys.argv[1] == "convert":
            value = float(sys.argv[2])
            from_unit = None
            to_unit = None

            i = 3
            while i < len(sys.argv):
                if sys.argv[i] == "--from":
                    from_unit = sys.argv[i + 1]
                    i += 2
                elif sys.argv[i] == "--to":
                    to_unit = sys.argv[i + 1]
                    i += 2
                else:
                    i += 1

            if from_unit is None or to_unit is None:
                print("Ошибка: нужно указать --from и --to", file=sys.stderr)
                sys.exit(2)

            result = convert(value, from_unit, to_unit)
            print(result)

        else:
            print("Неизвестная команда", file=sys.stderr)
            sys.exit(2)
    except CalculatorError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(2)

    sys.exit(0)
