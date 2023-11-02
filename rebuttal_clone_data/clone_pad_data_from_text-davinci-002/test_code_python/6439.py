def solution():
    days_per_week = 3
    initial_pushups = 10
    pushups_added_per_day = 5
    total_pushups = initial_pushups + (days_per_week * pushups_added_per_day)
    result = total_pushups
    return result

print(solution())