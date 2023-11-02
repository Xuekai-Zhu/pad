def solution():
    # Calculate the total number of pages Julie has left to read
    remaining_pages = 120 - 12 - 2*12  # Julie read 12 pages yesterday and 2*12 pages today

    # Calculate the number of pages Julie should read tomorrow to finish half of the remaining pages
    pages_to_read_tomorrow = remaining_pages / 2

    result = pages_to_read_tomorrow
    return result

print(solution())