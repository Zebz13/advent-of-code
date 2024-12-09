from inputs.day_7 import *
from itertools import product

operations = ["*","+"]

def calculator(left,right,operation):
    left,right = int(left),int(right)
    if operation == '+':
        return left + right
    elif operation == '*':
        return left * right
    elif operation =="||":
        return int(str(left)+str(right))

def evaluator(nums,operations):
    cum_sum = calculator(nums[0],nums[1],operations[0])
    for index in range(2,len(nums)):
        cum_sum = calculator(cum_sum,nums[index],operations[index-1])
    return cum_sum

def dynamic_looper(true_value,nums):
    for operation in product(['*','+','||'],repeat = len(nums) - 1):
        if(true_value == evaluator(nums,operation)):
            print(operation,evaluator(nums,operation))
            return true_value
    return 0

data = [j.split(": ") for j in data.split("\n")]
final_sum = 0
for i in data:
    eqn = int(i[0])
    args = i[1].split()
    print(args)
    final_sum+=dynamic_looper(eqn,args)
print(final_sum)
