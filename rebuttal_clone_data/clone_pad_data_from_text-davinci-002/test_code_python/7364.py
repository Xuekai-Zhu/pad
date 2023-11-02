def solution():
    hours_to_study = 4
    hours_available = hours_to_study - 0.5
    hours_per_chapter = 3
    hours_per_worksheet = 1.5
    break_time = 0.1
    snack_time = 0.3
    lunch_time = 0.5
    
    total_hours_study = (hours_per_chapter * 2) + (hours_per_worksheet * 4)
    total_hours_available = (hours_available * 4) - (break_time * 4) - (snack_time * 3) - (lunch_time)
    
    total_days_to_study = total_hours_study / total_hours_available
    result = total_days_to_study
    return result

print(solution())