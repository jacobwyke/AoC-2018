# Set the starting frequency
frequency = 0

# The location of the frequency input file
frequency_input_file = 'input.txt'

# List of all frequencies hit
frequencies = [frequency]

first_repeated_frequency = None

# read through the file
file = open(frequency_input_file, 'r')
changes = []
for line in file:
    changes.append(line)

while not first_repeated_frequency:
    for line in changes:
        # Get the value of the frequency change
        value = int(line[1:])
        if line[0] == '+':
            frequency += value
        else:
            frequency -= value

        # Check to see if this frequency has already been hit
        if frequency in frequencies:
           first_repeated_frequency = frequency
           break

        # Add the current frequency to the list
        frequencies.append(frequency)

print first_repeated_frequency

# 83130