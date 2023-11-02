def solution():
    """Jenna sets a goal of reading 600 pages a month for the month of September (which has 30 days). She knows that she'll be really busy at work the four weekdays starting on the 13th, so she won't have time to read. She can also read 100 pages on the 23rd, when she'll have a long boring flight. If she reads the same number of pages every other day, how many pages a day does she need to read?"""
    # Define the number of days Jenna has to read
    days_to_read = 30 - 4 - 1  # Subtract the 4 weekdays Jenna is busy and the day she'll spend reading on the flight

    # Subtract the 100 pages Jenna will read on the 23rd from her total goal for the month
    pages_left = 600 - 100

    # Divide the remaining pages by the number of days Jenna has to read them, to find out how many pages she needs to read each day.
    pages_per_day = pages_left / days_to_read

    # Display the number of pages Jenna needs to read each day
    result = pages_per_day
    return result

print(solution())