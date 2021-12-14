num = int(input())
var_1 = 0
var_2 = 0

""" 
We have three cases:
    1. Number is divisible but not a power of 2
    2. Number is not divisible by 2
    3. Number is divisible by 2 and a power of 2

 """
if num > 2:
    while num % 2 == 0:
        var_1 += 1
