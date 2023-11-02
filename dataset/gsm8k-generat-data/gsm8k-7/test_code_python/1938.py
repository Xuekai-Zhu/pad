def solution():
    num_math_books = 2
    math_book_cost = 3

    num_art_books = 3
    art_book_cost = 0  # unknown

    num_science_books = 6
    science_book_cost = 3

    total_cost = 30

    # Calculate the total cost of math and science books
    math_science_cost = (num_math_books + num_science_books) * math_book_cost

    # Calculate the total cost of all books except art books
    total_without_art = math_science_cost

    # Calculate the cost of each art book
    art_book_cost = (total_cost - total_without_art) / num_art_books
    result = art_book_cost
    return result

print(solution())