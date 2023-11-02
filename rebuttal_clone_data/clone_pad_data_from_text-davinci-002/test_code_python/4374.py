def solution():
    daily_servings_needed = 2
    number_of_days = 30
    total_servings_needed = daily_servings_needed * number_of_days
    servings_per_jar = 15
    number_of_jars_needed = total_servings_needed / servings_per_jar
    result = number_of_jars_needed
    return result

print(solution())