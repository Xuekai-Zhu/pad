def solution():
    total_pages = 158  # The book has 158 pages
    pages_read = 23 + 38 + 61  # Pages read from Monday to Wednesday
    pages_left = total_pages - pages_read  # Pages left to read
    days_left = 2  # Cora has two days left (Thursday and Friday) to finish the book

    # Calculate the number of pages Cora needs to read each day to finish the book in time
    pages_per_day = pages_left / days_left

    # Calculate the number of pages Cora needs to read on Thursday (assuming she reads twice as much on Friday)
    pages_on_thursday = pages_per_day / 3 * 2
    result = pages_on_thursday
    return result

print(solution())