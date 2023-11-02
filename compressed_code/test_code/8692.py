def solution():
    
    height = 5
    growth_per_year = 3
    age = 0
    
    while height < 23:
        age += 1
        height += growth_per_year
    
    result = age + 1 
    
    return result

print(solution())