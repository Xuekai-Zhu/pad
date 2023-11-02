def solution():
    books_cats = 7
    books_solar = 2
    magazines = 3
    price_book = 7
    price_magazine = 4

    # Calculate the total cost of books
    cost_books = (books_cats + books_solar) * price_book

    # Calculate the total cost of magazines
    cost_magazines = magazines * price_magazine

    # Calculate the total cost of everything
    total_cost = cost_books + cost_magazines
    result = total_cost
    return result

print(solution())