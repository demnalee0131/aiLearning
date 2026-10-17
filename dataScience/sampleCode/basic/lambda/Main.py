# lambda(anonymous) method/function examples


# pass the lambda function directly as a argument 
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]

result = apply_to_list(ints, lambda x: x * 2)
print(result)

# sort strings by the number of different word in each element
strings = ['foo', 
           'card',
           'bar',
           'aaaa',
           'abab',]
strings.sort(key = lambda x: len(set(x)))
print(strings)