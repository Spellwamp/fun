"""
Написати функцію is_year_leap, приймає 1 аргумент - рік, і повертає True, якщо рік
високосний, і False в іншому випадку.
"""
def isYearLeap(year):
    return 'Leap' if year % 100 != 0 and year % 4 == 0 or year % 400 == 0 else 'No leap year'

print(isYearLeap(2019))
