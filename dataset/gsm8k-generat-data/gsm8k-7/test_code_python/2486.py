def solution():
    total_pages = 248
    pages_per_hour = 16
    monday_hours = 3
    tuesday_hours = 6.5

    # Calculate the number of pages Joanna reads on Monday
    monday_pages = monday_hours * pages_per_hour

    # Calculate the number of pages Joanna reads on Tuesday
    tuesday_pages = tuesday_hours * pages_per_hour

    # Calculate the total number of pages Joanna reads in two days
    total_pages_read = monday_pages + tuesday_pages

    # Calculate the number of pages Joanna needs to read to finish the book
    remaining_pages = total_pages - total_pages_read

    # Calculate the number of hours Joanna needs to read to finish the book
    remaining_hours = remaining_pages / pages_per_hour
    result = remaining_hours
    return result

print(solution())