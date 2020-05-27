print('hello')

print("I'm going on a run")

print("hello \nworld")

print(len('test'))

mystring = "abcdefghijk"
print(mystring)

# indexing
print(mystring[3])
print(mystring[-1])

# slicing
print(mystring[2:])
print(mystring[:3])
print(mystring[3:6])
print(mystring[::2])
print(mystring[2:7:2])
print(mystring[::-1])

# concatenate String
name = "Sam"
last_letters = name[1:]
print('P' + last_letters)

x = 'hello world'
print(x + ' it is beautiful outside')
x = x + ' it is beautiful outside'
print(x + x)

letter = 'z'
print(letter * 10)

print('1' + '2')

# string methods
x = 'Hello World'
print(x.upper())
print(x.lower())
print(x.split())

x = "Hi this is a string"
print(x.split('i'))

# string formatting for printing
## .format()
print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

result = 100/777
print('The result was {r}'.format(r=result))
print('The result was {r:1.3f}'.format(r=result))
print('The result was {r:10.5f}'.format(r=result))

## fstring
name = "Mark"
print(f'Hello, his name is {name}')

name = "Sam"
age = 3
print(f'{name} is {age} years old')



