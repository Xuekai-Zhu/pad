def solution():
    """Carolyn practices the piano for 20 minutes a day and the violin for three times as long. If she practice six days a week, how many minutes does she spend practicing in a month with four weeks?"""
    # Define the time spent practicing piano and violin each day
    piano_time = 20
    violin_time = 3 * piano_time

    # Define the number of days Carolyn practices per week
    practice_days = 6

    # Calculate the total time spent practicing each day
    total_time = piano_time + violin_time

    # Calculate the total time spent practicing per week
    weekly_time = total_time * practice_days

    # Calculate the total time spent practicing in a month with four weeks
    monthly_time = weekly_time * 4

    result = monthly_time
    return result

print(solution())