def solution():
    """Justin needs to read at least 100 pages or more of his book in one week to pass his class. He has read 10 pages already on the first day. Assuming he reads twice the amount of pages as the first day each day in the remaining 6 days, how many pages will he have read after the week is over?"""
    # Define the number of pages read on the first day and the number of remaining days
    first_day_pages = 10
    remaining_days = 6

    # Define the multiplier for the doubling of pages each day
    multiplier = 2

    # Calculate the total number of pages read
    total_pages = first_day_pages
    for i in range(remaining_days):
        daily_pages = first_day_pages * multiplier**i
        total_pages += daily_pages

    # Display the total number of pages read
    result = total_pages
    return result

print(solution())