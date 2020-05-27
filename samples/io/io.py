myfile = open('c:/Users/emily/Desktop/python/samples/io/test.txt')
print(myfile.read())
print(myfile.read())

#resets cursor
myfile.seek(0)
contents = myfile.read()
print(contents)

myfile.seek(0)
print(myfile.readlines())

myfile.close()

with open('c:/Users/emily/Desktop/python/samples/io/test.txt') as my_new_file:
    contents = my_new_file.read()
    print('contents: ' + contents)

with open('c:/Users/emily/Desktop/python/samples/io/test.txt', mode='r') as myfile:
    contents = myfile.read()    
    print('READ: ' + contents)

with open('c:/Users/emily/Desktop/python/samples/io/my_new_file.txt', mode='r') as f:
    print(f.read())

with open('c:/Users/emily/Desktop/python/samples/io/my_new_file.txt', mode='a') as f:
    print(f.write('\nFOUR ON FOURTH'))

with open('c:/Users/emily/Desktop/python/samples/io/my_new_file.txt', mode='r') as f:
    print(f.read())

with open('c:/Users/emily/Desktop/python/samples/io/write.txt', mode='w') as f:
    f.write('I CREATED THIS FILE')

with open('c:/Users/emily/Desktop/python/samples/io/write.txt', mode='r') as f:
    print(f.read())




