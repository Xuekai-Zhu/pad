def solution():
    num_chapters = 2
    chapter_hours = 3
    num_worksheets = 4
    worksheet_hours = 1.5
    max_daily_hours = 4
    num_daily_breaks = (60 / 10) + 3 + (30 / 10)  # break every hour, 3 snack breaks, and 30 min lunch
    num_days = 0

    # Calculate the total hours needed for studying
    total_hours = (num_chapters * chapter_hours) + (num_worksheets * worksheet_hours)

    # Calculate the total number of days needed for studying
    while total_hours > 0:
        if total_hours <= max_daily_hours - num_daily_breaks:
            # if there is enough time left in the day, study for the remaining hours
            total_hours = 0
        else:
            # otherwise, study for the maximum hours possible and subtract daily breaks
            total_hours -= (max_daily_hours - num_daily_breaks)
            num_days += 1

    result = num_days
    return result

print(solution())