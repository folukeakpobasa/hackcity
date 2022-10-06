
def num_of_steps(num):
    steps = 0
    if num == 0 or num == 1:
        return 0
    while num > 0:
        if num % 2 == 1:
            floor_num = num // 2 
            
            num = floor_num - 1
            steps = steps + 1
        else:
            num = num / 2
            steps = steps + 1
    return steps

print(num_of_steps(14))
   
        
            
