def solution():
    shirt_time = 5
    pants_time = 3
    num_days_per_week = 5
    num_weeks = 4
    
    # Calculate total ironing time per day
    total_time_per_day = shirt_time + pants_time
    
    # Calculate total ironing time per week
    total_time_per_week = total_time_per_day * num_days_per_week
    
    # Calculate total ironing time over 4 weeks
    total_time_over_4_weeks = total_time_per_week * num_weeks
    
    result = total_time_over_4_weeks
    return result

print(solution())