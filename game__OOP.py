def add_element(collection):
    collection.append(0) 


some_list = [1,2,3]
add_element(some_list)
print(some_list)   

some_tuple = (1,2,3)
add_element(some_tuple)
print(some_tuple) 


import timeit

tuple_time = timeit.timeit('("apple", "banana", "cherry")[0]', number=1000000)
list_time = timeit.timeit('["apple", "banana", "cherry"][0]', number=1000000)

print("Время выполнения для кортежа:", tuple_time)
print("Время выполнения для списка:", list_time)


class MyContextManager:
    def __enter__(self):
        print("Выполняется предварительная работа")
        # Код перед выполнением блока кода

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выполняется завершающая работа")
        # Код после выполнения блока кода

# Использование менеджера контекста
with MyContextManager():
    print("Выполняется блок кода")