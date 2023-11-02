def solution():
    
    servings_per_day = 2
    days = 30
    jars_per_day = servings_per_day / 15
    total_jars = jars_per_day * days
    result = total_jars
    return result

print(solution())