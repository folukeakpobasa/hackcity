
def num_of_steps(num):
    steps = 0
    if num == 0 or num == 1:
        return 0
    while num > 0:
        if num % 2 == 1:
            floor_num = num // 2 
            
            num = floor_num - 1

        else:
            num /= 2
            
    
   
        
            
