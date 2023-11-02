def solution():
    pages_goal = 600  # Jenna's goal is to read 600 pages in September
    busy_days = 4  # Jenna will be busy at work for 4 weekdays starting on the 13th
    reading_days = 30 - busy_days - 1  # Subtract busy days and one day for the long boring flight
    extra_pages = 100  # Jenna will read an extra 100 pages on the 23rd

    # Calculate the total number of pages Jenna needs to read on non-busy days
    pages_to_read = pages_goal - extra_pages

    # Calculate the number of pages Jenna needs to read per day to meet her goal
    pages_per_day = pages_to_read / reading_days
    result = pages_per_day
    return result

print(solution())