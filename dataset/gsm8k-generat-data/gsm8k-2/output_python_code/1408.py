def solution():
    """Quinn's library was hosting a summer reading challenge. For every 5 books you read, you a coupon for a free donut at a nearby bakery. Quinn decided he could read 2 books a week for 10 weeks total. How many free donuts would Quinn be eligible for?"""
    books_per_week = 2
    total_weeks = 10
    total_books = books_per_week * total_weeks
    free_donuts = total_books // 5
    result = free_donuts
    return result

print(solution())