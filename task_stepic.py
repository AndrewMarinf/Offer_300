# 1 варик

def some_function(some_arg: list = []):
	some_arg.append(1)
	return some_arg


print(some_function()) # [1]
print(some_function()) # [1 1]
print(some_function())	# [1 1 1] 
print(some_function([2])) # [2,1]

print(some_function([1,6]))  # [1,6,1]
print(some_function())       # [1 1 1 1]
print(some_function())       # [1 1 1 1 1]
print(some_function([2,6,]))


def some_function(some_arg: list = None):
	if some_arg is None:
		some_arg = []
	some_arg.append(1)
	return some_arg


print(some_function())   # [1]
print(some_function())   # [1]
print(some_function())    # [1]

print(some_function([1,6])) # [1,6,1]
print(some_function())          # [1]
print(some_function())
print(some_function([2,6,]))