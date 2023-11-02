def solution():
    """James writes 10 pages an hour. If he writes 5 pages a day to 2 different people, how many hours a week does he spend writing?"""
    # Define the number of pages James writes per hour and the number of people he writes to
    PAGES_PER_HOUR = 10
    PEOPLE = 2

    # Calculate the total number of pages James writes per day
    daily_pages = PAGES_PER_HOUR * 5

    # Calculate the total number of pages James writes per week
    weekly_pages = daily_pages * 7

    # Calculate the total number of hours James spends writing per week
    hours_per_week = weekly_pages / (PAGES_PER_HOUR * PEOPLE)

    result = hours_per_week
    return result

print(solution())