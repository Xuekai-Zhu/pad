def solution():
    original_hours = 6
    increase_in_percent = 1/3
    # Calculate the increase in hours
    increase_in_hours = original_hours * increase_in_percent
    # Add the increase to the original hours
    new_hours = original_hours + increase_in_hours
    result = new_hours
    return result

print(solution())