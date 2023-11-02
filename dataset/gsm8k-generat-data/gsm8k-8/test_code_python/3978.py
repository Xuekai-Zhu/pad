def solution():
    # Calculate how many pages James writes per day
    daily_pages = 5 * 2

    # Calculate how many hours it takes James to write that many pages
    daily_hours = daily_pages / 10

    # Calculate how many hours James spends writing per week
    weekly_hours = daily_hours * 7
    result = weekly_hours
    return result

print(solution())