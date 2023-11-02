def solution():
    
    servings_per_day = 2
    servings_per_jar = 15
    days = 30
    total_servings_needed = servings_per_day * days
    jars_needed = total_servings_needed / servings_per_jar
    result = jars_needed
    return result

print(solution())