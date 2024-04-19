
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


print('для чего то надо ')
print('234324')
print(1234)
print(6 % 7)
print(234)
print(54678)
print('¯\\_(ツ)_//¯')
print(345324)
print(234123)
print(436)
print(345)


word = 'acbba'
def palindrome_check(word_) -> bool:
    pass


a = 2 
b = 6 
print('result: ', a + b)
result  = a + b 



sum = 0 
n = [7,5,8,11,2,5,4,2,2]
for i in n:
    if i % 2 ==0:
    sum += i
print(sum) 


scores = [1, 2, 3, 4, 5, 6, 7, 8, 9]

delete = [1,4,len(scores)-1]
delete.sort(reverse = True)
for ind in scores:
    del scores[delete] 
print(sorted)    
