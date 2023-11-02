def solution():
    # Calculate the total number of pages Sally reads in a day
    pages_per_day = 10/5 + 20/2  # 10 pages on weekdays and 20 pages on weekends

    # Calculate the total number of pages in the book
    total_pages = pages_per_day * 14  # 2 weeks = 14 days

    result = total_pages
    return result

print(solution())