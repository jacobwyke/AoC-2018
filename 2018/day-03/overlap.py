# The location of the input file
input_file = 'input.txt'

gridsize = 1500

# read through the file and break out the data
file = open(input_file, 'r')
cuts = []
for line in file:
    parts = line.split(' ')
    start = parts[2].split(',')
    size = parts[3].split('x')
 
    cut = {
        'id': parts[0][1:],
		'start': [
            int(start[0]),
            int(start[1][:-1])
        ],
		'size': [
		    int(size[0]),
            int(size[1].strip())
		]
	}
    cuts.append(cut)

# create our grid
grid = [[0] * gridsize ] * gridsize

total = 0

for cut in cuts:
    print cut
    row = cut['start'][0]
    column = cut['start'][1]
    width = cut['size'][0]
    height = cut['size'][1]
    total += (width * height)
    for y in range(height):
        for x in range(width):
            print "%s, %s" % (column + x, row + y)
            grid[column + x][row + y] += 1
            
#print grid
print total
print 1000 * 1000
