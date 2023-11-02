def solution():
    """Lance wants to finish reading a 100 page book in 3 days. Yesterday, he started to read 35 pages. Today, he read 5 fewer pages than yesterday. How many pages should he read tomorrow to finish the book?"""
    # Define the total number of pages and the number of days left
    total_pages = 100
    days_left = 3

    # Calculate the number of pages Lance has already read
    pages_read = 35 + (35 - 5) # Today he read 5 fewer pages than yesterday

    # Calculate the number of pages Lance needs to read to finish the book
    pages_left = total_pages - pages_read

    # Calculate the number of pages Lance needs to read each day
    pages_per_day = pages_left / days_left

    # Calculate the number of pages Lance needs to read tomorrow
    pages_tomorrow = pages_per_day

    # return the result
    result = pages_tomorrow
    return result

print(solution())