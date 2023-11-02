def solution():
    # Define the amount of money June has and the cost of each type of book
    money = 500
    math_book_cost = 20
    science_book_cost = 10
    art_book_cost = 20

    # Calculate the total cost of the math books
    math_books = 4
    math_books_cost = math_books * math_book_cost

    # Calculate the total cost of the science books
    science_books = math_books + 6
    science_books_cost = science_books * science_book_cost

    # Calculate the total cost of the art books
    art_books = 2 * math_books
    art_books_cost = art_books * art_book_cost

    # Calculate the total cost of all the books
    total_books_cost = math_books_cost + science_books_cost + art_books_cost

    # Calculate how much money she spent on music books
    music_books_cost = money - total_books_cost
    result = music_books_cost
    return result

print(solution())