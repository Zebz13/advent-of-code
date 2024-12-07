from inputs.day_6 import *

lines = data.split('\n')

for i_count,line in enumerate(lines):
    for j_count,cells in enumerate(line):
        if cells == '^':
            guard_init = [i_count,j_count]
            break

guard_directions = [[-1,0],[0,1],[1,0],[0,-1]]
guard_route = set()
flag = 1
temp_i,temp_j = guard_init[0],guard_init[1]
while 0<=temp_i<len(lines) and 0<=temp_j<len(lines[0]):
    for i_move,j_move in guard_directions:
        while(0<=temp_i<len(lines) and 0<=temp_j<len(lines[0]) and lines[temp_i][temp_j]!='#'):
            if (temp_i,temp_j) not in guard_route:
                guard_route.add((temp_i,temp_j))
            temp_i,temp_j = temp_i + i_move, temp_j+j_move
        if(not(0<=temp_i<len(lines)) or not(0<=temp_j<len(lines[0]))):
            flag = 0
            break
        temp_i,temp_j = temp_i - i_move, temp_j-j_move
    if(not flag):
        break
print(len(guard_route))

def create_copy(arr):
    temp_arr = [[0] * len(arr[0]) for _ in range(len(arr))]
    for count_i,val_i in enumerate(arr):
        for count_j,val_j in enumerate(val_i):
            temp_arr[count_i][count_j] = val_j
    return temp_arr


loop_counter = 0
sample_count = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        temp_lines = create_copy(lines)
        temp_i,temp_j = guard_init[0],guard_init[1]
        # print(f"{i},{j}")
        if(temp_lines[i][j]!='#' and (i!=guard_init[0] or j!= guard_init[1])):
            # print(i,j,temp_lines[i][j])
            sample_count+=1
            temp_lines[i][j] = '#'
        direction_set = set()
        flag = 1
        # if(i == 6 and j == 3):
        #     print("hell")
        while 0<=temp_i<len(temp_lines) and 0<=temp_j<len(temp_lines[0]):
            for i_move,j_move in guard_directions:
                # print(f"i moves {i_move},{j_move}")
                while(0<=temp_i<len(temp_lines) and 0<=temp_j<len(temp_lines[0]) and temp_lines[temp_i][temp_j]!='#'):
                    # print(temp_i,temp_j,i_move,j_move)
                    if (temp_i,temp_j,i_move,j_move) not in direction_set:
                        direction_set.add((temp_i,temp_j,i_move,j_move))
                    else:
                        flag = 0
                        # print((temp_i,temp_j,i_move,j_move))
                        loop_counter+=1
                        break
                    temp_i,temp_j = temp_i + i_move, temp_j+j_move
                    # print(temp_i,temp_j)
                    # print(temp_lines)
                    # print(0<=temp_i<len(temp_lines), 0<=temp_j<len(temp_lines[0]))
                if((not(0<=temp_i<len(temp_lines)) or not(0<=temp_j<len(temp_lines[0]))) or not flag):
                    flag = 0
                    break
                temp_i,temp_j = temp_i - i_move, temp_j-j_move
            if(not flag):
                break
print(loop_counter)
# print(sample_count)