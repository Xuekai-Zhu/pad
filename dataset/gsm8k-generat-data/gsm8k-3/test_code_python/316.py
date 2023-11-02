def solution():
    """Berry wants to make sure he reads an average of 50 pages a day. This week he read 43 pages on Sunday, 65 pages on Monday, and 28 pages on Tuesday. He had a soccer game and fell asleep early on Wednesday so he read nothing. On Thursday he read 70 pages, and on Friday he read 56 pages. How many pages does he have to read on Saturday to reach his goal?"""
    # Define the average pages per day and days in the week
    AVERAGE_PAGES_PER_DAY = 50
    DAYS_IN_WEEK = 7

    # Calculate the total pages read so far
    total_pages_read = 43 + 65 + 28 + 0 + 70 + 56

    # Calculate the pages needed to reach the average
    pages_needed = AVERAGE_PAGES_PER_DAY * DAYS_IN_WEEK - total_pages_read

    # Display the pages needed to reach the goal
    result = pages_needed
    return result

print(solution())