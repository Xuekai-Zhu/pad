def solution():
    
    starting_temp = 20
    target_temp = 100
    heat_rate = 5
    minutes = (target_temp - starting_temp) / heat_rate
    result = minutes
    return result

print(solution())