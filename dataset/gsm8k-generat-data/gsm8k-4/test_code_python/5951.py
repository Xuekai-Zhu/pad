def solution():
    """Cora started reading a 158-page book on Monday, and she decided she wanted to finish it by the end of Friday. She read 23 pages on Monday, 38 pages on Tuesday, and 61 pages on Wednesday. She knows she will have time to read twice as much on Friday as she does on Thursday. How many pages does she have to read on Thursday to finish the book in time?"""
    # Define the total number of pages in the book
    total_pages = 158

    # Calculate the number of pages read from Monday to Wednesday
    pages_read = 23 + 38 + 61

    # Calculate the number of pages left to read
    pages_left = total_pages - pages_read

    # Calculate the number of days left to read
    days_left = 2

    # Calculate the number of pages Cora needs to read per day to finish the book in time
    pages_per_day = pages_left / days_left

    # Calculate the number of pages Cora needs to read on Thursday to finish the book in time
    pages_on_thursday = pages_per_day / 3

    result = pages_on_thursday
    return result

print(solution())