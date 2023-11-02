def solution():
    
    day_one_squats = 30
    increase_per_day = 5
    day_two_squats = day_one_squats + increase_per_day
    day_three_squats = day_two_squats + increase_per_day
    day_four_squats = day_three_squats + increase_per_day
    day_after_tomorrow_squats = day_three_squats + increase_per_day
    result = day_after_tomorrow_squats
    return result

print(solution())