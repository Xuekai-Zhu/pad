def solution():
    """Carolyn practices the piano for 20 minutes a day and the violin for three times as long. If she practice six days a week, how many minutes does she spend practicing in a month with four weeks?"""
    # Define the time spent practicing piano and violin per day
    piano_time_per_day = 20
    violin_time_per_day = 3 * piano_time_per_day

    # Calculate the total time spent practicing per week
    total_time_per_week = piano_time_per_day + violin_time_per_day
    total_time_per_week *= 6

    # Calculate the total time spent practicing in a month with four weeks
    total_time_per_month = total_time_per_week * 4

    # Return the result
    result = total_time_per_month
    return result

print(solution())