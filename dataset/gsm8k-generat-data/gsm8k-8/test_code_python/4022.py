def solution():
    # Calculate the total time James spends meditating each day in minutes
    daily_meditation_time = 30 * 2
    
    # Calculate the total time James spends meditating each week in minutes
    weekly_meditation_time = daily_meditation_time * 7
    
    # Convert weekly meditation time to hours
    weekly_meditation_hours = weekly_meditation_time / 60
    
    result = weekly_meditation_hours
    return result

print(solution())