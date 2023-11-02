def solution():
    """Lance wants to finish reading a 100 page book in 3 days. Yesterday, he started to read 35 pages. Today, he read 5 fewer pages than yesterday. How many pages should he read tomorrow to finish the book?"""
    # Define the number of pages Lance has left to read
    pages_left = 100 - 35

    # Calculate how many pages Lance read today
    pages_today = 35 - 5

    # Calculate how many pages Lance has to read tomorrow
    pages_tomorrow = pages_left - pages_today

    # Display the number of pages Lance has to read tomorrow
    result = pages_tomorrow
    return result

print(solution())