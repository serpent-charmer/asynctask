"""TODO: task."""

import hashlib


def hashlines(lines):
    """Выводит хэшированные строки.

    Parameters:
        lines: строки.

    Returns:
        хэшированные строки.
    """
    hashed = hashlib.sha256(bytes(''.join(lines), 'UTF-8'))
    return hashed.digest()


def getvactext():
    """Возвращает название вакансии и ожидаемый диапазон зарплаты через год.

    Returns:
        название вакансии и ожидаемый диапазон зарплаты через год.
    """
    vac_name = 'Стажёр-программист Python / Python Developer Trainee'
    lowest, highest = (29000, 67000)
    return '{0} вилка {1} {2}'.format(vac_name, lowest, highest)
