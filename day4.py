from inputs.day_4 import *

array_list = data.split('\n')


directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
i_lim = len(array_list)
j_lim = len(array_list[0])
count = 0
for start_i in range(i_lim):
    for start_j in range(j_lim):
        if(array_list[start_i][start_j] == 'X'):
            for i_move,j_move in directions:
                temp_i,temp_j = start_i,start_j
                temp_val = "XMAS"
                flag = 1
                for _ in range(1,4):
                    temp_i,temp_j = temp_i+i_move,temp_j+j_move
                    if(0<=temp_i<i_lim and 0<=temp_j<j_lim and temp_val[_] == array_list[temp_i][temp_j]):
                        continue
                    else:
                        flag = 0
                        break
                if(flag):
                    # print(start_i,start_j)
                    count+=1
print(count)


directions = {(1,1):(-1,-1),(-1,1):(1,-1)}
i_lim = len(array_list)
j_lim = len(array_list[0])
count = 0
for start_i in range(i_lim):
    for start_j in range(j_lim):
        if(array_list[start_i][start_j] == 'A'):
            for i_move,j_move in directions:
                temp_val = ['M','S']
                temp_i,temp_j = start_i+i_move,start_j+j_move
                temp_i_val,temp_j_val = start_i + directions[(i_move,j_move)][0], start_j + directions[(i_move,j_move)][1]
                flag = 1
                if(0<=temp_i<i_lim and 0<=temp_j<j_lim and 0<=temp_i_val<i_lim and 0<=temp_j_val<j_lim and array_list[temp_i][temp_j] in temp_val):
                    temp_val.remove(array_list[temp_i][temp_j])
                    try:
                        temp_val.remove(array_list[temp_i_val][temp_j_val])
                    except:
                        flag = 0
                        break
                else:
                    flag = 0
                    break
            if(flag and not temp_val):
                # print(start_i,start_j)
                count+=1
print(count)