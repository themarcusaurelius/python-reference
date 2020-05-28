#can pass through multiple arguments as a tuple using *{random}
def myfunc(*args):
    # Returns 5% of the sum of a & b
    return sum(args) * 0.05
result = myfunc(40,60,30)
print(result)

#can use arbitrary number of keys
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
result = myfunc(fruit='apple',veggie='lettuce')

#####
def myfunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

result = myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')
print(result)