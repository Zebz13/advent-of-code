from inputs.day_5 import *
from collections import defaultdict

def validPage(rule_dict,line_arr):
    for i in range(len(line_arr)):
        for j in range(i-1,-1,-1):
            if(line_arr[j] in rule_dict[line_arr[i]]):
                return False
    return True

def sortPage(rule_dict,line_arr):
    updatedLine = []
    temp_arr = line_arr.copy()
    init = 0
    while(temp_arr and init<len(temp_arr)):
        flag = 1
        for j in temp_arr[init+1:]:
            if(temp_arr[init] in rule_dict[j]):
                flag = 0
                break
        if(flag):
            updatedLine.append(temp_arr[init])
            temp_arr.pop(init)
            init=0
        else:
            init+=1
    return updatedLine

rules,pages = data.split('\n\n')

rule_dict = defaultdict(list)
for large,small in [i.split('|') for i in rules.split('\n')]:
    rule_dict[large].append(small)

invalid_to_valid_lines = []
valid_lines = []
for lines in [page.split(',') for page in pages.split('\n')]:
    if(not validPage(rule_dict,lines)):
        invalid_to_valid_lines.append(sortPage(rule_dict,lines))

cum_sum = 0
for lines in invalid_to_valid_lines:
    cum_sum+=int(lines[int(len(lines)/2)])
print(cum_sum)
