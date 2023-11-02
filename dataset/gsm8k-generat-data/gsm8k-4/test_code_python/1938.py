def solution():
    """Alicia has to buy some books for the new school year. She buys 2 math books, 3 art books, and 6 science books, for a total of $30. If both the math and science books cost $3 each, what was the cost of each art book?"""
    # Define the prices of math and science books
    math_price = 3
    science_price = 3

    # Define the number of books bought
    math_books = 2
    art_books = 3
    science_books = 6

    # Calculate the total cost of the books
    total_cost = math_books * math_price + art_books * x + science_books * science_price

    # Solve for x, the cost of each art book
    x = (30 - math_books * math_price - science_books * science_price) / art_books

    # return the result
    result = round(x, 2)
    return result

print(solution())