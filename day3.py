from inputs.day_3 import *
import re

regex_part1 = r"mul\(\d{1,3},\d{1,3}\)"

multiply_list = re.findall(regex_part1,data)
operands = [mult.replace("mul(",'').replace(")",'').split(',') for mult in multiply_list]
output = sum([int(operand[0]) * int(operand[1]) for operand in operands ])
print(output)

regex_part2 = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"

multiply_list = re.findall(regex_part2,data)
final_list = []
flag = 1
for i in range(len(multiply_list)):
    if(multiply_list[i]=="don't()"):
        flag = 0
    elif(multiply_list[i]=="do()"):
        flag = 1
    if(multiply_list[i] not in ("don't()","do()") and flag):
        final_list.append(multiply_list[i])
operands = [mult.replace("mul(",'').replace(")",'').split(',') for mult in final_list]
output = sum([int(operand[0]) * int(operand[1]) for operand in operands ])
print(output)


