def solution():
    num_chickens_start = 4
    num_chickens_end = num_chickens_start * 8
    num_eggs_per_chicken_per_day = 6
    num_days_per_week = 7

    # Calculate the total number of eggs collected per day
    total_num_eggs_per_day = num_chickens_end * num_eggs_per_chicken_per_day

    # Calculate the total number of eggs collected per week
    total_num_eggs_per_week = total_num_eggs_per_day * num_days_per_week
    result = total_num_eggs_per_week
    return result

print(solution())