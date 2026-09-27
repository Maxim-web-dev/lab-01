import pytest

from toolkit.converter import convert
from toolkit.errors import (
    BelowAbsoluteZeroError,
    IncompatibleUnitsError,
    UnknownUnitError,
)


def test_converter_1():
    assert convert(1000, "mm", "m") == 1.0


def test_converter_2():
    assert convert(1.5, "kg", "g") == 1500.0


def test_converter_3():
    assert convert(0, "c", "f") == 32.0


def test_converter_4():
    assert convert(-273.15, "c", "k") == pytest.approx(0.0, abs=1e-6)


def test_converter_5():
    assert convert(1000, "MM", "M") == 1.0


def test_converter_6():
    with pytest.raises(BelowAbsoluteZeroError):
        convert(-300, "c", "f")


def test_converter_7():
    with pytest.raises(IncompatibleUnitsError):
        convert(1, "kg", "m")


def test_converter_8():
    with pytest.raises(UnknownUnitError):
        convert(1, "efwwef", "m")
