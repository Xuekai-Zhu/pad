def solution():
    
    serving_size = 0.5
    servings_per_day = 3
    ounces_in_quart = 32
    container_size = ounces_in_quart - 2
    total_servings = container_size / serving_size
    days_last = total_servings / servings_per_day
    result = days_last
    return result

print(solution())