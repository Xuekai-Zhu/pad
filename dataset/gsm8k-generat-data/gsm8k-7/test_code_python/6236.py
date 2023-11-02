def solution():
    total_words = 1000
    words_per_half_hour = 300
    num_half_hours = (total_words - 200) / words_per_half_hour
    
    # Calculate the total time in minutes it will take Abigail to finish the report
    total_time_minutes = num_half_hours * 30
    
    result = total_time_minutes
    return result

print(solution())