def solution():
    
    current_sleep = 6
    increase = current_sleep * (1/3)
    new_sleep = current_sleep + increase
    result = new_sleep
    return result

print(solution())