def solution():
    
    stars_per_jar = 85
    stars_already_made = 33
    jars_needed = 4
    total_stars_needed = jars_needed * stars_per_jar - stars_already_made
    result = total_stars_needed
    return result

print(solution())