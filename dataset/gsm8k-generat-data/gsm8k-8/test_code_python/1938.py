def solution():
    # Define the cost of the math and science books
    math_and_science_cost = 2 * 3 + 6 * 3

    # Calculate the cost of the art books
    art_books_cost = 30 - math_and_science_cost

    # Calculate the cost of one art book
    cost_per_art_book = art_books_cost / 3
    result = cost_per_art_book
    return result

print(solution())