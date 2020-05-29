def square(num):
    return num**2
my_nums = [1,2,3,4,5]
for item in map(square, my_nums):
    print(item)

########### String Splicer
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Salty']
result = list(map(splicer,names))
print(result)

########### Even Number
def check_even(num):
    return num%2 == 0 

mynums = [1,2,3,4,5,6]
result = list(filter(check_even,mynums))
print(result)

########## Lambdas
square = lambda num: num ** 2
result = square(5)
print(result)

result = list(map(lambda num:num**2, mynums))
print(result)

result = list(filter(lambda num:num%2 == 0, mynums))
print(result)

result = list(map(lambda x:x[0],names))
print(result)

result = list(map(lambda name:name[::-1],names))
print(result)

