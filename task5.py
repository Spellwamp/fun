"""
Користувач робить внесок в розмірі n гривень строком на years років під 10% річних
(щороку розмір його внеску збільшується на 10%. Ці гроші додаються до суми вкладу, і на них
в наступному році теж будуть відсотки).

Написати функцію bank, яка приймає аргументи n і years, і повертає суму, яка буде на
рахунку користувача.
"""
def bank(n, year):
    return '{:.1f}'.format(eval(str(n) + '*' +'1.' + str(year)))

print(bank(1939, 30))