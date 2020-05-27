x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else: 
    print("X IS NOT LESS THAN 5")

x = [1,2,3,]

for item in x:
    # comment
    pass 

print("end of my script")
     
mystring = "Sammy"

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1 