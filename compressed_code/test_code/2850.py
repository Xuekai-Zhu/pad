def solution():
    
    initial_height = 5
    growth_rate = 3
    target_height = 23
    age = 0
    while initial_height < target_height:
        initial_height += growth_rate
        age += 1
    result = age + 1  
    return result

print(solution())