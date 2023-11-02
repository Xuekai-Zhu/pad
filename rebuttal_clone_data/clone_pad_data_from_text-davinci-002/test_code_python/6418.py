def solution():
    goal_miles_per_week = 24
    miles_per_day = 3
    days_run = 6
    miles_left = goal_miles_per_week - (miles_per_day * days_run)
    result = miles_left
    return result

print(solution())