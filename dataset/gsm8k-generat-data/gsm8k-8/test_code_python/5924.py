def solution():
    sandwiches_per_day = 10
    days_in_week = 7
    sandwiches_in_week = sandwiches_per_day * days_in_week
    apples_per_sandwich = 4
    total_apples_eaten = sandwiches_in_week * apples_per_sandwich
    result = total_apples_eaten
    return result

print(solution())