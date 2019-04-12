"""
Написати функцію date, яка приймає 3 аргументи - день, місяць і рік. Повернути True,
якщо така дата є в нашому календарі, і False - в іншому випадку.
"""
def data(day, month, year):
    from datetime import date
    try:
        date(year=year, month=month, day=day)
        return True
    except:
        return False
    
print(data(31, 12, 2019))
