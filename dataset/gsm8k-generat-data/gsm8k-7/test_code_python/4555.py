def solution():
    num_eggs = 40
    eggs_per_day = 2
    days_per_week = 5 # assuming Maddy only eats eggs on weekdays

    # Calculate the total number of days Maddy will have chocolate eggs
    total_days = num_eggs / eggs_per_day

    # Calculate the total number of weeks Maddy will have chocolate eggs
    total_weeks = total_days / days_per_week
    result = total_weeks
    return result

print(solution())