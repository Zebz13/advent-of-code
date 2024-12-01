def part1(data_set_a,data_set_b):
    data_sets = zip(sorted(data_set_a),sorted(data_set_b))
    cum_sum = 0
    for a,b in data_sets:
        cum_sum += abs(int(a)-int(b))
    return cum_sum

def part2(data_set_a,data_set_b):
    temp_dict_for_b = {}
    for i in data_set_b:
        temp_dict_for_b[i] = temp_dict_for_b.get(i,0) +1
    cum_sum = 0
    for i in data_set_a:
        cum_sum+= int(i) * temp_dict_for_b.get(i,0)
    return cum_sum

#put everything as string in a sepearate file - so I can add it to gitignore
from inputs.day_1 import *
data_sets = star1.split("\n")
data_sets.remove('')
data_set_a = [i.split("   ")[0] for i in data_sets]
data_set_b = [i.split("   ")[1] for i in data_sets]

print(part1(data_set_a,data_set_b))
print(part2(data_set_a,data_set_b))


