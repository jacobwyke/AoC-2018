import sys

sys.setrecursionlimit(150000)

# The location of the input file
input_file = 'input.txt'

# read through the file and get the data
file = open(input_file, 'r')
with open(input_file, 'r') as polymer_file:
    polymer_string = polymer_file.read().replace('\n', '')

def polymer_check(polymer_array, starting_index):
    '''
    Function that takes array of letters and then removes
    any duplicate letters that are mixed cases of the same letter.
    '''
    index = starting_index
    
    while index < len(polymer_array):
        if index >= len(polymer_array) - 1:
            return polymer_array
            
        current_char = polymer_array[index]
        next_char = polymer_array[index + 1]
        if current_char.islower():
            if current_char.upper() == next_char:
                polymer_array.pop(index + 1)
                polymer_array.pop(index)
                return polymer_check(polymer_array, index - 1)
        else:
            if current_char.lower() == next_char:
                polymer_array.pop(index + 1)
                polymer_array.pop(index)
                return polymer_check(polymer_array, index - 1)
        
        index += 1
    
    return polymer_array

# Get the answer for the first question
result = polymer_check(list(polymer_string), 0)
print len(result)

#
# Second Challenge
#

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
data = {}

for letter in letters:
    cleaned_string = polymer_string.replace(letter, '').replace(letter.upper(), '')
    data[letter] = len(polymer_check(list(cleaned_string), 0))
    
print data
