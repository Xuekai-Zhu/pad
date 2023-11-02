def solution():
    """Quinn's library was hosting a summer reading challenge.  For every 5 books you read, you a coupon for a free donut at a nearby bakery.  Quinn decided he could read 2 books a week for 10 weeks total.  How many free donuts would Quinn be eligible for?"""
    # Define the number of books Quinn can read per week and the total number of weeks
    books_per_week = 2
    weeks = 10

    # Calculate the total number of books Quinn will read
    total_books = books_per_week * weeks

    # Calculate the number of free donuts Quinn is eligible for
    free_donuts = total_books // 5

    # Display the number of free donuts
    result = free_donuts
    return result

print(solution())