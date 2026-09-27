import pytest

from toolkit.calculator.calculations import calculate
from toolkit.errors import (
    CalculatorError,
    DivisionByZeroError,
    EmptyExpressionError,
    ManyDotsError,
    ManyNumbersError,
    ManyOperatorsError,
    OperatorAtTheEndError,
    OperatorInTheBegginingError,
)


def test_calculator_1():
    assert calculate("2+3*4") == 14


def test_calculator_2():
    assert calculate("10 / 4") == 2.5


def test_calculator_3():
    assert calculate("-2 * -3") == 6


def test_calculator_4():
    assert calculate("1+-2") == -1


def test_calculator_5():
    assert calculate("10-2-3") == 5


def test_calculator_6():
    assert calculate("2*3*4*5") == 120


def test_calculator_7():
    assert calculate("1.5+2.5") == 4.0


def test_calculator_8():
    with pytest.raises(EmptyExpressionError):
        calculate("")


def test_calculator_9():
    with pytest.raises(ManyOperatorsError):
        calculate("2*/3")


def test_calculator_10():
    with pytest.raises(CalculatorError):
        calculate("2+a")


def test_calculator_11():
    with pytest.raises(ManyNumbersError):
        calculate("2 3")


def test_calculator_12():
    with pytest.raises(DivisionByZeroError):
        calculate("1/0")


def test_calculator_13():
    with pytest.raises(ManyDotsError):
        calculate("1.2.3")


def test_calculator_14():
    with pytest.raises(OperatorInTheBegginingError):
        calculate("*2+3")


def test_calculator_15():
    with pytest.raises(OperatorAtTheEndError):
        calculate("2+3*")
