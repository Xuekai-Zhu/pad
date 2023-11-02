def solution():
    # Calculate the total number of pages James writes per day
    daily_pages = 5 * 2  # he writes 5 pages to 2 different people
    # Calculate the total number of hours James spends writing per day
    daily_hours = daily_pages / 10  # he writes 10 pages an hour
    # Calculate the total number of hours James spends writing per week
    weekly_hours = daily_hours * 7
    result = weekly_hours
    return result

print(solution())