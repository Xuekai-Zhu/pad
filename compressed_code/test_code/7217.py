def solution():
    
    num_fish = 6
    num_fish *= 2**2  
    num_fish -= num_fish // 3  
    num_fish *= 2**2  
    num_fish -= num_fish // 4  
    num_fish *= 2**2  
    num_fish += 15  
    result = num_fish
    return result

print(solution())