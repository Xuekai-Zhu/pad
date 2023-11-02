def solution():
    deadlift_at_13 = 300
    percent_increase = 250
    deadlift_at_18 = (percent_increase / 100) * deadlift_at_13 + 100
    pounds_added_per_year = (deadlift_at_18 - deadlift_at_13) / 5
    result = pounds_added_per_year
    
    return result

print(solution())