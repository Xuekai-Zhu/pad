def solution():
    # Pages written on Monday
    pages_monday = 60 / 30  # Mack writes 1 page every 30 minutes
    # Pages written on Tuesday
    pages_tuesday = 45 / 15  # Mack writes 1 page every 15 minutes
    # Pages written on Wednesday
    pages_wednesday = 5

    # Total pages written
    total_pages = pages_monday + pages_tuesday + pages_wednesday
    result = total_pages
    return result

print(solution())