def solution():
    """Jenna sets a goal of reading 600 pages a month for the month of September (which has 30 days). She knows that she'll be really busy at work the four weekdays starting on the 13th, so she won't have time to read. She can also read 100 pages on the 23rd, when she'll have a long boring flight. If she reads the same number of pages every other day, how many pages a day does she need to read?"""

    # Define the number of pages she needs to read in September
    goal_pages = 600

    # Define the number of days she has available to read
    available_days = 30 - 4 - 1  # subtracting the 4 busy workdays and the long flight day

    # Define the number of pages she can read on the flight day
    flight_pages = 100

    # Calculate the number of pages she still needs to read
    remaining_pages = goal_pages - flight_pages

    # Calculate the number of pages she needs to read per day to reach her goal
    pages_per_day = remaining_pages / available_days

    result = pages_per_day
    return result

print(solution())