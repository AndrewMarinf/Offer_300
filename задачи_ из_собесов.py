
import copy 

def foo(a: dict) -> dict:
    a = copy.deepcopy(a)
    # b = a.copy()
    a['z'] = 99
    return a

dict1 = {1:'a',2:'b',3:'c',4:'d'}

dict2 = foo(dict1)

print(dict1)
print(dict2)


print(id(dict1))
print(id(dict2))



print(6 % 7)
