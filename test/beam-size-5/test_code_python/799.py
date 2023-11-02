def solution():
    
    # Define the total number of hours playing
    total_hours = 30

    # Define the number of hours Kris plays each day
    daily_hours = 0.5
    weekly_hours = 2

    # Calculate the total number of hours Kris plays in 2 weeks
    total_hours_2_weeks = daily_hours * 2 * 2 * 2

    # Calculate the total number of hours Kris still needs to play
    remaining_hours = total_hours - total_hours_2_weeks

    # return the result
    result = remaining_hours
    return result

print(solution())