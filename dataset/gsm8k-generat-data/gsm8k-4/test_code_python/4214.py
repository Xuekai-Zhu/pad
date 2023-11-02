def solution():
    """June has $500 for buying school supplies for the new school year. She buys four maths books at $20 each, six more science books than maths books at $10 each, and twice as many art books as maths books at $20 each. If she also bought music books, how much money did she spend on music books?"""
    # Define the initial budget and the cost of each type of book
    budget = 500
    math_price = 20
    science_price = 10
    art_price = 20

    # Calculate the cost of the math books
    math_books = 4
    math_cost = math_books * math_price

    # Calculate the cost of the science books
    science_books = math_books + 6
    science_cost = science_books * science_price

    # Calculate the cost of the art books
    art_books = math_books * 2
    art_cost = art_books * art_price

    # Calculate the total cost of all the books
    total_cost = math_cost + science_cost + art_cost

    # Calculate the money spent on music books
    music_cost = budget - total_cost

    # Return the result
    result = music_cost
    return result

print(solution())