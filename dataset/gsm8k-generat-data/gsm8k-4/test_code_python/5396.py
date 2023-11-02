def solution():
    """Justin needs to read at least 100 pages or more of his book in one week to pass his class. He has read 10 pages already on the first day. Assuming he reads twice the amount of pages as the first day each day in the remaining 6 days, how many pages will he have read after the week is over?"""
    # Define the number of pages read on the first day
    day_one = 10

    # Calculate the total number of pages read after the week
    total_pages = day_one + (day_one * 2) + (day_one * 2 * 2) + (day_one * 2 * 2 * 2) + (day_one * 2 * 2 * 2 * 2) + (day_one * 2 * 2 * 2 * 2 * 2)

    # Return the result
    result = total_pages
    return result

print(solution())