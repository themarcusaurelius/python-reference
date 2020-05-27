## range()
for num in range(0,10,2):
    print(num)

print(list(range(0,10,2)))

## enumerate()
index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

word = "abcde"

for item,index in enumerate(word):
    print(item)
    print(letter)
    print('\n')

## zip()
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for item in zip(mylist1,mylist2,mylist3):
    print(item)

print(list(zip(mylist1,mylist2)))

## in
print('x' in [1,2,3])
print('x' in ['x','y','z'])
print('a' in 'a world')
print('mykey' in {'mykey':345})

## min() max()
mylist = [10,20,30,40]
print(min(mylist))
print(max(mylist))

## random library
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))

## input()
result = input('What is your name? ')
print(f'Your name is {result}')

result = input('What is your favorite number? ')
print(f'Your favorite number is {int(result)}')