def solution():
    """June has $500 for buying school supplies for the new school year. She buys four maths books at $20 each, six more science books than maths books at $10 each, and twice as many art books as maths books at $20 each. If she also bought music books, how much money did she spend on music books?"""
    # Define the cost of each type of book
    MATH_BOOK_PRICE = 20
    SCIENCE_BOOK_PRICE = 10
    ART_BOOK_PRICE = 20

    # Define the number of each type of book purchased
    math_books = 4
    science_books = math_books + 6
    art_books = math_books * 2

    # Calculate the total cost of the math books
    math_cost = math_books * MATH_BOOK_PRICE

    # Calculate the total cost of the science books
    science_cost = science_books * SCIENCE_BOOK_PRICE

    # Calculate the total cost of the art books
    art_cost = art_books * ART_BOOK_PRICE

    # Calculate the total cost of all the books
    total_cost = math_cost + science_cost + art_cost

    # Calculate the amount spent on music books
    music_cost = 500 - total_cost

    # Display the amount spent on music books
    result = music_cost
    return result

print(solution())