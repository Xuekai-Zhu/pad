def solution():
    
    initial_sugar = 24
    sugar_per_hour = 4
    hours_passed = 3
    remaining_sugar = initial_sugar - (sugar_per_hour * hours_passed)
    hours_needed = remaining_sugar / sugar_per_hour
    result = hours_needed
    return result

print(solution())