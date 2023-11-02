def solution():
    frequency = 3
    average_kg = 200
    first_week_extra_garbage = average_kg * frequency
    second_week_average_garbage = first_week_extra_garbage / 2
    total_garbage = first_week_extra_garbage + second_week_average_garbage
    result = total_garbage
    
    return result

print(solution())