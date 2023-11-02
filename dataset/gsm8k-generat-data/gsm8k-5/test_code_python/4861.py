def solution():
    pages_per_minute = 4/2  # Amalia reads 4 pages in 2 minutes, so she reads 2 pages per minute
    pages_to_read = 18  # Amalia wants to read 18 pages
    time_to_read = pages_to_read / pages_per_minute  # Calculate how many minutes it will take her to read 18 pages

    result = time_to_read
    return result

print(solution())