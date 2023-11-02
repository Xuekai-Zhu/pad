def solution():
    # Calculate the total cost of maths books
    maths_books_cost = 4 * 20  # Four maths books at $20 each

    # Calculate the number of science books June bought
    science_books_count = 4 + 6  # June bought six more science books than maths books

    # Calculate the total cost of science books
    science_books_cost = science_books_count * 10  # Science books cost $10 each

    # Calculate the number of art books June bought
    art_books_count = 2 * 4  # June bought twice as many art books as maths books

    # Calculate the total cost of art books
    art_books_cost = art_books_count * 20  # Art books cost $20 each

    # Calculate the total amount spent on all books
    total_spent_on_books = maths_books_cost + science_books_cost + art_books_cost

    # Calculate the amount June has left after buying books
    amount_left = 500 - total_spent_on_books

    # Assume she spent all the remaining amount on music books
    music_books_cost = amount_left
    result = music_books_cost
    return result

print(solution())