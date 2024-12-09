from inputs.day_8 import *

grid = [list(j) for j in data.split("\n")]

antenna_dict = {}
rows = len(grid)
cols = len(grid[0])

for row in range(rows):
    for col in range(cols):
        if(grid[row][col]!='.'):
            if(grid[row][col] in antenna_dict):
                antenna_dict[grid[row][col]].append((row,col))
            else:
                antenna_dict[grid[row][col]] = [(row,col)]

def find_antinodes(arr_of_antennas):
    n = len(arr_of_antennas)
    antinode_arr = set()
    for i in range(n-1):
        for j in range(i+1,n):
            x1,y1 = arr_of_antennas[i]
            x2,y2 = arr_of_antennas[j]
            x_diff,y_diff = x1-x2,y1-y2
            #add the value and absolute value
            if(0<=x1+x_diff<rows and 0<=y1+y_diff<cols):
                antinode_arr.add((x1+x_diff,y1+y_diff))
            if(0<=x2+(-1*x_diff)<rows and 0<=y2+(-1*y_diff)<cols):
                antinode_arr.add((x2+(-1*x_diff),y2+(-1*y_diff)))
    return antinode_arr


def find_antinodes_all(arr_of_antennas):
    n = len(arr_of_antennas)
    antinode_arr = set()
    for i in range(n-1):
        for j in range(i+1,n):
            x1,y1 = arr_of_antennas[i]
            x2,y2 = arr_of_antennas[j]
            x_diff,y_diff = x1-x2,y1-y2
            #add the value and absolute value
            antinode_arr.add((x1,y1))
            antinode_arr.add((x2,y2))
            while(0<=x1+x_diff<rows and 0<=y1+y_diff<cols):
                antinode_arr.add((x1+x_diff,y1+y_diff))
                x1,y1 = x1+x_diff,y1+y_diff
            while(0<=x2+(-1*x_diff)<rows and 0<=y2+(-1*y_diff)<cols):
                antinode_arr.add((x2+(-1*x_diff),y2+(-1*y_diff)))
                x2,y2 = x2+(-1*x_diff),y2+(-1*y_diff)
    # print(antinode_arr)
    return antinode_arr

final_set = set()
# print(antenna_dict)
for antenna_freq in antenna_dict:
    final_set |= find_antinodes(antenna_dict[antenna_freq])
print(len(final_set))

final_set_2 = set()
# print(antenna_dict)
for antenna_freq in antenna_dict:
    # print(antenna_freq)
    final_set_2 |= find_antinodes_all(antenna_dict[antenna_freq])
print(len(final_set_2))