a = 123
b = 123
print(id(a))
print(id(b))

g = [1,2,3]
h = [1,2,3]
print(id(g))
print(id(h))

print(a is b)
print(a == b)
print(g is h)
print(g == h)


# контекстный менеджер 
with open('file.txt','r') as file:
    i = file.read()
    print(i)


#  1 Пример реализации своего контекстного менеджера на основе класса:
import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"Время выполнения: {elapsed_time} секунд")

# Пример использования контекстного менеджера Timer
with Timer() as timer:
    # Код, который нужно измерить по времени
    time.sleep(5)



# 2  Пример реализации своего контекстного менеджера на основе класса:
import sqlite3
 
class DataConn:
 
    def __init__(self, db_name):
        """Конструктор"""
        self.db_name = db_name
    
    def __enter__(self):
        """
        Открываем подключение с базой данных.
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    
    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закрываем подключение.
        """
        self.conn.close()
        if exc_val:
            raise
 
if __name__ == '__main__':
    db = 'test.db'
    
    with DataConn(db) as conn:
        cursor = conn.cursor()    


class Menedger:
    def __enter__(self):
        print('enter')

    def __exit__(self):
        print('exit')    

with Menedger() as menedger:
    print('hello')


# Гениратор списка
a = [0 for i in range(1,10+1)]
print(a) 
a = [i**3 for i in range(1,5)]
print(a)

# Выражение гениратор c круглыми скобками 
b = (i**3 for i in range(1,5))
print(sum(b))
print(sum(b))


# итерируемый объект например список
s = [1,2,3]        
#print(next(s)) # он не представляет собой итератор!!!!!!
d = iter(s) # iter функция итератор
print(next(d))
print(next(d))  # итератор всегда хранит какой объект будет браться следующим 

c = (i for i in range(1,20))
for i in c:
    print(i)

c = (i for i in range(1,20))
print(min(c))
print(max(c))
print(sorted(c))
print(sum(c))

dg = [1,2,3]
sd = [1,2,3]
print(dg == sd )
print(dg is sd )

lo = 2080
la = 2080
print(lo == la)
print(lo is la)



words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon', 'drop', 'produce', 'acquisition',
         'cheap', 'strength', 'master', 'perception', 'noise', 'strange', 'am']

lens = (len(i) for i in words)

for i in lens:
    print(i)    



def f():
    return [34,32,54]

print(f())
print(f())

def f_g():
    for i in [34,72,54]:
        yield i
# print(next(f_g()))   
# print(next(f_g()))

s = f_g()
print(next(s))
print(next(s))


 
# глубокая и поверхстнотная копия

a = [1,[2]]
b = a
b.append(3) 
print(a)    # [1, [2], 3]
print(b)    # [1, [2], 3]
b[1].append(4)  
print(a)    #[1, [2,4], 3]
print(b)    #[1, [2,4 ], 3]

# поверхностная копия
import copy 
b = copy.copy(a) # объект a скопирвоался в новую память
b.append(10)   # добавили только в b
print(a)     # [1, [2, 4], 3]
print(b)     # [1, [2, 4], 3, 10]
b[1].append(5)       # так как b[1] это один и тот же объект в a и b по этому вставка произойдет везде
print(a)     # [1, [2, 4, 5], 3]
print(b)     # [1, [2, 4, 5], 3, 10]

print(id(a))
print(id(b))
print('*' * 20)

# глубокая копия 
import copy 
b = copy.deepcopy(a) # объект a скопирвоался в новую память
b.append(10)   # добавили только в b
print(a)     # [1, [2, 4], 3]
print(b)     # [1, [2, 4], 3, 10]
b[1].append(6)       # полная копия
print(a)     # [1, [2, 4, 5], 3]
print(b)     # [1, [2, 4, 5,6], 3, 10]


def some_function(some_arg: list = []):
	some_arg.append(1)
	return some_arg

print(some_function())
print(some_function())
print(some_function())

print(some_function([3,6]))
print(some_function())
print(some_function())
print(some_function([2,6,]))


tuple1 = (1, 2, 3)
list1 = [1, 2, 3]

# Ошибка! Кортежи не могут быть изменены
# tuple1[0] = 4

# Работает! Списки могут быть изменены
list1[0] = 4


a = ([],2)
a[0].append(3) # вывод([3], 2)


x = '1,000,000'
print(x[2:9])
print(x.count('1'))
print(x * 3)
print(int(x))

age = 12 
print('ребенок 'if age <= 18 else  'dphjcksq ')





import copy

original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)

# Проверка: изменение копии не влияет на оригинал
deep_copy[2][0] = 5
print(original_list)  # [1, 2, [3, 4]]
print(deep_copy)  # [1, 2, [5, 4]]

print(id(original_list ))
print(id(deep_copy ))

# ===============================================================================
import copy

original_list = [1, 2, [3, 4]]
shallow_copy = copy.copy(original_list)

# Проверка: изменение копии влияет на оригинал
shallow_copy[2][0] = 5
print(original_list)  # [1, 2, [5, 4]]
print(shallow_copy)  # [1, 2, [5, 4]]

print(id(original_list ))
print(id(shallow_copy))
