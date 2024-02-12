# Написать функцию, которая возвращает медиану массива. 

# На вход дается отсортированный массив, на выход - ожидается число.

# Медиана массива считается как средний элемент, если кол-во элементов нечетное.
# Если четное - как среднее арифметическое между центральными элементами

# a = [1,2,3]

# # моя медиана
# def median(mas: list):
#     if len(mas)%2 == 0:
#         return 


# находим медиану
def find_median(x):
    if len(x) % 2 == 0:
        return (x[len(x) // 2] + x[len(x) // 2 -1]) / 2
    else:
        return x[len(x) // 2]

print(find_median(a))



b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_median(x):
    # Сначала сортируем список x в порядке возрастания
    x.sort()

    # Получаем длину списка
    length = len(x)

    # Проверяем, является ли длина списка четной
    if length % 2 == 0:
        # Если да, то находим индексы двух центральных элементов
        index1 = length // 2 # тут половина массива
        index2 = index1 - 1  # тут получаем его индекс
        
        # Возвращаем среднее значение двух центральных элементов
        return (x[index1] + x[index2]) / 2
    else:
        # Если длина списка нечетная, находим индекс центрального элемента
        index = length // 2 #тут получаем элемент который в середине тут не float, а целое только число
        
        # Возвращаем индекс центральный элемент
        return x[index]


print(find_median(b))   





