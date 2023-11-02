def solution():
    total_pages = 140  # The book has 140 pages
    pages_per_day_initial = 3 * 6  # Jessy plans to read 3 times, 6 pages each time, every day of the week
    days = 7  # Jessy has a week to finish reading the book

    # Calculate the total pages Jessy will actually read using her initial plan
    pages_read_initial = pages_per_day_initial * days

    # Calculate the additional pages Jessy needs to read to achieve her goal
    additional_pages = total_pages - pages_read_initial

    # Calculate the additional pages Jessy needs to read per day
    additional_pages_per_day = additional_pages / days
    result = additional_pages_per_day
    return result

print(solution())