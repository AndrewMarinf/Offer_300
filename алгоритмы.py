

"""Пузырьковый метод"""

list_ = [6,3,4,9,7,2,5]
count = 0

def py(listes) -> list:
    n = len(listes)
    for run in range(n - 1 ): # ЭТО СКОЛЬКО НАДО ОБХОДОВ СДЕЛАТЬ, обходов надо сделать на единицу меньше чем колличество элементов
        for i in range(n-1): # мы обходим все элементы кроме последнего ,так как его нет ,после 9 нет ничего !!!! 
            if listes[i]>listes[i+1]: # listes[i] это 6 , listes[i+1] это 3 
                global count   # а то глобальную переменную не поменяем !!! ахахах 
                count += 1
                listes[i],listes[i+1] = listes[i+1],listes[i]
                print(list_)       
    return listes

print(py(list_))
print(count)










a = [325,567,3532,868,346]
count = 0


def f(h):
    n = len(h)
    for run_count in range(n-1):
        for i in range(n-1):
            global count
            if h[i]> h[i+1]:
                count += 1 
                h[i],h[i+1] = h[i+1],h[i]
    return h            


print(f(a))
print(count)