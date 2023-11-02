def solution():
    
    fries_only = 15 - 6 
    burgers_only = 10 - 6 
    both = 6 
    neither = 25 - (fries_only + burgers_only + both) 
    result = neither
    return result

print(solution())