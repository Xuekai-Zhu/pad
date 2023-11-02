def solution():
    
    days_left = 3
    remaining_goal = 1000 - 300 - 40
    houses_per_visit = 4
    money_per_visit = 10
    visits_per_day = remaining_goal / (days_left * money_per_visit)
    houses_per_day = visits_per_day * houses_per_visit
    result = houses_per_day
    return result

print(solution())