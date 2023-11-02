def solution():
    # Calculate the total amount of money spent on maths books
    maths_books = 4  # June bought 4 maths books
    maths_books_cost = 20  # Each maths book costs $20
    total_maths_cost = maths_books * maths_books_cost

    # Calculate the total amount of money spent on science books
    science_books = maths_books + 6  # June bought 6 more science books than maths books
    science_books_cost = 10  # Each science book costs $10
    total_science_cost = science_books * science_books_cost

    # Calculate the total amount of money spent on art books
    art_books = maths_books * 2  # June bought twice as many art books as maths books
    art_books_cost = 20  # Each art book costs $20
    total_art_cost = art_books * art_books_cost

    # Calculate the total amount of money spent on all books
    total_books_cost = total_maths_cost + total_science_cost + total_art_cost

    # Calculate the amount of money spent on music books
    music_books_cost = 500 - total_books_cost  # June has $500 and spent the rest on music books
    result = music_books_cost
    return result

print(solution())