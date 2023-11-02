def solution():
    total_pages = 180 + 100  # Yasna has two books: 180 pages and 100 pages
    days = 14  # Yasna wants to finish both books in 2 weeks, which is 14 days

    # Calculate the number of pages Yasna needs to read every day
    pages_per_day = total_pages / days
    result = pages_per_day
    return result

print(solution())