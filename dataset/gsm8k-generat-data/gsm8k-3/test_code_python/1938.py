def solution():
    """Alicia has to buy some books for the new school year. She buys 2 math books, 3 art books, and 6 science books, for a total of $30. If both the math and science books cost $3 each, what was the cost of each art book?"""
    # Define the cost of each math and science book
    MATH_SCIENCE_COST = 3

    # Define the number of each type of book purchased
    math_books = 2
    art_books = 3
    science_books = 6

    # Calculate the total cost of the math and science books
    math_science_cost = (math_books + science_books) * MATH_SCIENCE_COST

    # Calculate the cost of each art book
    art_book_cost = (30 - math_science_cost) / art_books

    # Display the cost of each art book
    result = art_book_cost
    return result

print(solution())