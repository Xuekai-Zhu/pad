def solution():
    pages_per_hour = 10  # James writes 10 pages per hour
    pages_per_day = 5  # James writes 5 pages per day to 2 different people
    people = 2  # James writes to 2 different people
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total number of pages James writes in a week
    total_pages = pages_per_day * people * days_per_week

    # Calculate the total number of hours James spends writing in a week
    total_hours = total_pages / pages_per_hour
    result = total_hours
    return result

print(solution())