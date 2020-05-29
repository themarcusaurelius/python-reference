#LEGB Rule
#L : Local -  Names assigned in any way within a function (def or lambda), andnot declared global in that function
#E : Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer
#G : Global (module) - Names assigned at the top-level of a module file, or declared global in a def within the file
#B : Built-in (Python) - Names preassigned in the built-in names module: open, range, SyntaxError

#Local
lambda num:num**2

#Enclosing function local
#GLOBAL
name = 'GLOBAL'

def greet():
    #ENCLOSING
    name = 'ENCLOSING'

    def hello():
        #LOCAL
        name = 'LOCAL'
        print('Hello ' + name)
    hello()
greet()

#GLOBAL
x = 50

def func():
    global x
    print(f'X is {x}')

    #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE
    x = 200
    print(f'I JUST LOCALLY CHANGED X to {x}')
func()
print(x)

#Cleaner and safer than the blobal keyword with larger scripts
def func(x):
    print(f'X is {x}')

    #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED X to {x}')
    return x
x = func(x)
print(x)

