"""
Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає
пору року, якій цей місяць належить (зима, весна, літо або осінь).
"""
def season(x):
    if x <= 3:
        return 'Winter'
    elif 3 < x <= 6:
        return 'Spring'
    elif 6 < x <= 9:
        return 'Summer'
    else: return 'Autumn'

print(season(10))
