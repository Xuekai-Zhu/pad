def solution():
    """James writes 10 pages an hour.  If he writes 5 pages a day to 2 different people, how many hours a week does he spend writing?"""
    # Define the number of pages James writes per hour
    PAGES_PER_HOUR = 10

    # Define the number of pages James writes per day to each person
    PAGES_PER_DAY = 5

    # Define the number of people James is writing to
    PEOPLE = 2

    # Calculate the total number of pages James writes per week
    pages_per_week = PAGES_PER_DAY * PEOPLE * 7

    # Calculate the number of hours James spends writing per week
    hours_per_week = pages_per_week / PAGES_PER_HOUR

    # Display the number of hours spent writing per week
    result = hours_per_week
    return result

print(solution())