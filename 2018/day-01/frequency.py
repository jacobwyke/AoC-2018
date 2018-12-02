# Set the starting frequency
frequency = 0

# The location of the frequency input file
frequency_input_file = 'input.txt'

# read through the file
file = open(frequency_input_file, 'r')
for line in file:
    # Get the value of the frequency change
    value = int(line[1:])
    if line[0] == '+':
        frequency += value
    else:
        frequency -= value

# Print the frequency at the end
print frequency

# 587