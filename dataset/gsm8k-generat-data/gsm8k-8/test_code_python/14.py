def solution():
    # Calculate how many pages Joy can read per minute
    pages_per_minute = 8 / 20

    # Calculate how many minutes it will take her to read 120 pages
    minutes_to_read_120_pages = 120 / pages_per_minute

    # Convert minutes to hours
    hours_to_read_120_pages = minutes_to_read_120_pages / 60

    result = hours_to_read_120_pages
    return result

print(solution())