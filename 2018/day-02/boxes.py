# The location of the input file
input_file = 'input.txt'

# read through the file
file = open(input_file, 'r')
IDs = []
for line in file:
    IDs.append(line)

# Loop through each ID
for ID in IDs:
    matches = [0] * len(IDs)

    # Loop through each char
    for char_index in range(len(ID)):
        # Compare with other IDs
        for id_index in range(len(IDs)):
            check_id = IDs[id_index]
            if check_id is not ID:
                if ID[char_index] == check_id[char_index]:
                    matches[id_index] += 1

    for index in range(len(matches)):
        count = matches[index]
        if count > 25:
            string_1 = ID
            string_2 = IDs[index]
            common = ""

            for id_index in range(len(string_1)):
                if string_1[id_index] == string_2[id_index]:
                    common = common + string_1[id_index]

            print string_1
            print string_2
            print common