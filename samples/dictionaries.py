my_dictionary = {'key1':'value1', 'key2':'value2'}
print(my_dictionary)
print(my_dictionary['key1'])

prices_lookup = {'apples': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup['apples'])

d = {'k1': 123, 'k2': [0,1,2], 'k3': {'insideKey': 100}}
print(d['k2'])
print(d['k3']['insideKey'])
print(d['k2'][2])

d = {'key1': ['a','b','c']}
mylist = d['key1']
print(mylist)

letter = mylist[2]
print(letter.upper())
print(d['key1'][2].upper())

d = {'k1': 100, 'k2': 200}
d['k3'] = 300
print(d)

# methods
d = {'k1': 100, 'k2': 200, 'k3': 300}

## .keys()
print(d.keys())

## .values()
print(d.values())

## .items()
print(d.items())

