def solution():
    # Calculate the total number of minutes Carl types in 4 hours per day
    minutes_per_day = 4 * 60  # 4 hours is 240 minutes

    # Calculate the total number of words Carl types in one day
    words_per_day = 50 * minutes_per_day 

    # Calculate the total number of words Carl can type in 7 days
    words_7_days = words_per_day * 7
    result = words_7_days
    return result

print(solution())