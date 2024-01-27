from random import uniform


def add_years_to_date(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result


def wear_sensors():
    sensors = [uniform(0, 1) for n in range(2)] + [0, 1]
    return sensors
