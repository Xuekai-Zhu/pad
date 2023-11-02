def solution():
    
    num_amoebae = 16
    days_per_division = 2
    num_divisions = 0
    
    while num_amoebae > 1:
        num_amoebae /= 2
        num_divisions += 1
        
    result = num_divisions * days_per_division
    return result

print(solution())