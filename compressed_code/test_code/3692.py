def solution():
    
    initial_sugar = 24
    sugar_per_hour = 4
    harvested_sugar = sugar_per_hour * 3
    remaining_sugar = initial_sugar - harvested_sugar
    additional_hours_needed = remaining_sugar / sugar_per_hour
    result = additional_hours_needed
    return result

print(solution())