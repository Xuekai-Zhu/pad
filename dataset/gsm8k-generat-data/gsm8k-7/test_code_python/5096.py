def solution():
    weekdays = 5
    weekend_days = 2
    week_length = 7
    weekday_pages = 10
    weekend_pages = 20
    total_weeks = 2

    # Calculate the total number of pages Sally reads on weekdays
    total_weekday_pages = weekdays * weekday_pages * week_length

    # Calculate the total number of pages Sally reads on weekends
    total_weekend_pages = weekend_days * weekend_pages * week_length

    # Calculate the total number of pages Sally reads in two weeks
    total_pages = total_weekday_pages + total_weekend_pages

    result = total_pages
    return result

print(solution())