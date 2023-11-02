def solution():
    # Subtract the 4 weekdays where Jenna won't have time to read
    available_days = 30 - 4

    # Subtract the one day where Jenna will read 100 pages
    available_pages = 600 - 100

    # Divide the remaining pages by the remaining days to find pages per day
    pages_per_day = available_pages / available_days
    result = pages_per_day
    return result

print(solution())