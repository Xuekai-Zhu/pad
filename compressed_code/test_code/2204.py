def solution():
    
    first_day_surfers = 1500
    second_day_surfers = first_day_surfers + 600
    third_day_surfers = (2/5) * first_day_surfers
    total_surfers = first_day_surfers + second_day_surfers + third_day_surfers
    average_surfers = total_surfers / 3
    result = average_surfers
    return result

print(solution())