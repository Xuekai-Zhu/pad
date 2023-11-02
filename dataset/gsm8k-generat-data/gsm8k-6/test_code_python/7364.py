def solution():
    # Calculate the total study time for the 2 chapters and 4 worksheets
    chapter_time = 3 * 2  # 3 hours for each of the 2 chapters
    worksheet_time = 1.5 * 4  # 1.5 hours for each of the 4 worksheets
    total_time = chapter_time + worksheet_time  # total study time

    # Calculate the total time for breaks and lunch
    break_time = (10/60) * 7 * 3  # 10-minute break every hour, 3 snack breaks per day, for 7 days
    lunch_time = (30/60) * 7  # 30 minutes for lunch each day, for 7 days
    total_break_lunch_time = break_time + lunch_time  

    # Calculate the total time available for studying each day
    available_time = 4 - (10/60) - (total_break_lunch_time/7)  

    # Calculate the number of days needed for total study time
    days_needed = total_time / available_time
    result = days_needed
    return result

print(solution())