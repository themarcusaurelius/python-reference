# def name_function(name='NAME'):
#     '''
#     DOCSTRING: Information about the function
#     INPUT: no input
#     OUTPUT: Hello..
#     '''
#     print('Hello ' + name)

# help(name_function)
# name_function()

def name_function(name='NAME'):
    return 'Hello ' + name

result = name_function('Mark')
print(result)

#####
def add(n1,n2):
    return n1+n2

result = add(5,10)
print(result)

######
# Find out if the word "dog" is in a string
def dog_check(mystring):
    return 'dog' in mystring.lower()
        
result = dog_check('Dog ran away')
print(result)

# Pig Latin
def pig_latin(word):
    first_letter = word[0]

    # Check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    
    return pig_word

word = input('What is the word you would like to translate? ')
result = pig_latin(f'{word}')
print(f'{word} is {result}')