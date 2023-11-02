def solution():
    budget = 500
    num_maths_books = 4
    maths_book_price = 20
    num_science_books = num_maths_books + 6
    science_book_price = 10
    num_art_books = num_maths_books * 2
    art_book_price = 20

    # Calculate the total cost of all maths books
    total_maths_books_cost = num_maths_books * maths_book_price

    # Calculate the total cost of all science books
    total_science_books_cost = num_science_books * science_book_price

    # Calculate the total cost of all art books
    total_art_books_cost = num_art_books * art_book_price

    # Calculate the total cost of all books
    total_books_cost = total_maths_books_cost + total_science_books_cost + total_art_books_cost

    # Calculate the total amount spent on everything but music books
    total_spent = total_books_cost

    # Calculate the amount spent on music books
    spent_on_music_books = budget - total_spent
    result = spent_on_music_books
    return result

print(solution())