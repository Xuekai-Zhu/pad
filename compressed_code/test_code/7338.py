def solution():
    
    candies_per_hour = 50
    production_goal = 4000
    hours_per_day = 10
    candies_per_day = candies_per_hour * hours_per_day
    days_to_complete = production_goal // candies_per_day
    if production_goal % candies_per_day != 0:
        days_to_complete += 1
    result = days_to_complete
    return result

print(solution())