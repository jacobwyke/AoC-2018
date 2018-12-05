# The location of the input file
input_file = 'input.txt'

gridsize = 1000

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

def print_grid(grid):
    for row in grid:
        print(*row)
        
# create our grid
grid = [['0' for x in range(gridsize)] for y in range(gridsize)]

for cut in cuts:
    row = cut['start'][1]
    column = cut['start'][0]
    width = cut['size'][0]
    height = cut['size'][1]
    
    for y in range(height):
        for x in range(width):
            space = grid[row + y][column + x]
            
            if space == '0':
                grid[row + y][column + x] = cut['id']
            else:
                grid[row + y][column + x] = 'X'
            
count = 0            
for x in grid:
    count += x.count('X')

print(count)

for cut in cuts:
    row = cut['start'][1]
    column = cut['start'][0]
    width = cut['size'][0]
    height = cut['size'][1]
    
    overlaps = False
    
    for y in range(height):
        for x in range(width):
            space = grid[row + y][column + x]
            
            if space != cut['id']:
                overlaps = True
    
    if not overlaps:
        print(cut['id'])
