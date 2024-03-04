

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


"""ВСЕ НУЛИ В КОНЕЦ"""
l = [1, 0, 9, 6, 0, 12, 3]

def moveZeroes( nums: list[int]) -> None:
        last_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:               
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1
        return l               


print(moveZeroes(l))                