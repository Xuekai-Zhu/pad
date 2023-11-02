def solution():
    """Jay bought a book for $25, a pen for $4, and a ruler for $1. He paid with a fifty-dollar bill. How much change, in dollars, did Jay get?"""
    # Define the cost of the book, pen, and ruler
    book_cost = 25
    pen_cost = 4
    ruler_cost = 1

    # Calculate the total cost of the items
    total_cost = book_cost + pen_cost + ruler_cost

    # Calculate the amount of change
    change = 50 - total_cost
    
    # return the result
    result = change
    return result

print(solution())