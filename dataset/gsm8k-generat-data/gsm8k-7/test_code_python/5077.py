def solution():
    total_pages = 100
    days_left = 3
    pages_read_yesterday = 35
    pages_read_today = pages_read_yesterday - 5

    # Calculate the remaining pages that Lance needs to read
    remaining_pages = total_pages - pages_read_yesterday - pages_read_today

    # Calculate the number of pages Lance needs to read per day to finish the book on time
    pages_per_day = remaining_pages / days_left

    # Calculate the number of pages Lance should read tomorrow
    pages_to_read_tomorrow = pages_per_day - pages_read_today
    result = pages_to_read_tomorrow
    return result

print(solution())