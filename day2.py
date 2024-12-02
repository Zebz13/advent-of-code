from math import copysign

def good_label(label):
    for i in range(len(label) - 1):
        sign = copysign(1, label[0] - label[1])
        if (
            (1 <= label[i] - label[i + 1] <= 3) or (-1 >= label[i] - label[i + 1] >= -3)
        ) and sign == copysign(1, label[i] - label[i + 1]):
            pass
        else:
            return (-1, i, i + 1)
    return 1

def part1(labels):
    count = 0
    for label in labels:
        if(good_label(label) == 1):
            count+=1
    return count

def part2(labels):
    count = 0
    for label in labels:
        flag_for_success = 0
        for i in range(len(label)):
            if(good_label(label[:i] + label[i+1:]) == 1):
                flag_for_success = 1
                break
        if(flag_for_success):
            count+=1
    return count


# put everything as string in a sepearate file - so I can add it to gitignore
from inputs.day_2 import *

reports = data.split("\n")
labels = [list(map(int, i.split(" "))) for i in reports]

print(part2(labels))
# print(part1(data_set_a,data_set_b))
# print(part2(data_set_a,data_set_b))
