mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)

for num in mylist:
    print('Hello')

for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(f'Even number: {num}')
    else:
        print(f'Odd number: {num}')

######
list_sum = 0 

for num in mylist:
    list_sum = list_sum + num

print(list_sum)

######
mystring = 'Hello World'

for letter in mystring:
    print(letter)

for _ in 'Hello World':
    print('Cool!')

######
tup = (1,2,3)

for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]

print(len(mylist))

for item in mylist:
    print(item)

## tuple unpackibng
for a,b in mylist:
    print(a)

mylist = [(1,2,3,),(5,6,7,),(8,9,10)]

for a,b,c in mylist:
    print(b)

## dictionary unpacking
d = {'k1': 1, 'k2':2, 'k3':3}

for item in d.items():
    print(item)

for item in d:
    print(item)

for key,value in d.items():
    print(value)