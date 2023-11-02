def solution():
    bowl_size = 10 #in ounces
    servings_per_minute = 5
    soup_size = 6 * 128 #in ounces
    total_servings = soup_size / bowl_size
    minutes_to_serve = total_servings / servings_per_minute
    rounded_minutes = round(minutes_to_serve)
    result = rounded_minutes
    return result

print(solution())