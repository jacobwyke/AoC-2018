# The location of the input file
input_file = 'input.txt'

two_appearances = 0
three_appearances = 0

# read through the file
file = open(input_file, 'r')
for line in file:
    occurance = {}
    two = 0
    three = 0

    # loop through each character in the line
    for character in line:
        if character in occurance.keys():
            occurance[character] += 1
        else:
            occurance[character] = 1

    # See if we have any characters that appear multiple times in this ID
    for letter, count in occurance.items():
        if count == 2:
            two = 1
        elif count == 3:
            three = 1

    # Count the occurances of double or tripple letters in this ID
    if two:
        two_appearances += 1
    if three:
        three_appearances += 1

print two_appearances
print three_appearances
print two_appearances * three_appearances

# 247
# 30
# 7410