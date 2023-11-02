def solution():
    num_books = 3
    pages_read_monday = 20
    pages_read_tuesday = 12
    total_pages_read = 51

    # Calculate the total number of pages Nico read on Monday and Tuesday
    pages_read_mon_tues = pages_read_monday + pages_read_tuesday

    # Calculate the total number of pages Nico read on Wednesday
    pages_read_wednesday = total_pages_read - pages_read_mon_tues

    result = pages_read_wednesday
    return result

print(solution())