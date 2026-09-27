from toolkit.errors import (
    BelowAbsoluteZeroError,
    IncompatibleUnitsError,
    UnknownUnitError,
)

# Коэффициенты перевода в базовую единицу группы (метр для длины, грамм для массы)
LENGTH_TO_METERS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
}

MASS_TO_GRAMS = {
    "g": 1,
    "kg": 1000,
}

# Список различных температурых единиц
TEMPERATURE_UNITS = {"c", "f", "k"}


# Определяем, к какой группе относится единица. Если не нашли нигде - вызываем ошибку.
def which_unit_group(unit: str) -> str:
    if unit in LENGTH_TO_METERS:
        return "length"
    if unit in MASS_TO_GRAMS:
        return "mass"
    if unit in TEMPERATURE_UNITS:
        return "temperature"
    raise UnknownUnitError(unit)


# Переводим значение в градусы Цельсия - берем ее как базовую для температуры
def to_celsius(value: float, unit: str) -> float:
    if unit == "c":
        return value
    if unit == "f":
        return (value - 32) * 5 / 9
    return value - 273.15  # unit == "k"


# Из градусов Цельсия переводим обратно в нужную единицу
def from_celsius(celsius: float, unit: str) -> float:
    if unit == "c":
        return celsius
    if unit == "f":
        return celsius * 9 / 5 + 32
    return celsius + 273.15  # unit == "k"


# Длина и масса переводятся одинаково: через общий коэффициент в базовую единицу
def convert_by_ratio(value: float, from_unit: str, to_unit: str, ratios: dict) -> float:
    value_in_base = value * ratios[from_unit]
    return value_in_base / ratios[to_unit]


# Конвертируем. Регистр приводим к нижнему
def convert(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.strip().lower()
    to_unit = to_unit.strip().lower()

    from_group = which_unit_group(from_unit)
    to_group = which_unit_group(to_unit)

    # Конвертация между разными группами запрещена
    if from_group != to_group:
        raise IncompatibleUnitsError((from_unit, to_unit))

    if from_group == "length":
        return float(convert_by_ratio(value, from_unit, to_unit, LENGTH_TO_METERS))

    if from_group == "mass":
        return float(convert_by_ratio(value, from_unit, to_unit, MASS_TO_GRAMS))

    celsius_value = to_celsius(value, from_unit)
    # Проверка абсолютного нуля
    if celsius_value < -273.15:
        raise BelowAbsoluteZeroError(value)

    return float(from_celsius(celsius_value, to_unit))
