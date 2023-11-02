def solution():
    start_day = 1
    end_day = 12
    pages_per_day = 8
    progress = 2/3  # two-thirds of the book

    # Calculate the total number of days that Bill read
    num_days = end_day - start_day + 1

    # Calculate the total number of pages that Bill read
    total_pages_read = pages_per_day * num_days

    # Calculate the total number of pages in the book
    total_pages = total_pages_read / progress
    result = total_pages
    return result

print(solution())