def solution():
    frequency_per_week = 4
    duration_per_session = 2
    num_years = 10
    
    # Calculate the total number of weeks in 10 years
    total_weeks = num_years * 52
    
    # Calculate the total number of hours Tom danced
    total_hours = total_weeks * frequency_per_week * duration_per_session
    result = total_hours
    return result

print(solution())