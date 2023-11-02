def solution():
    num_books_whales = 9
    num_books_fish = 7
    num_magazines = 3

    book_price = 11
    magazine_price = 1

    # Calculate the total cost of all books
    total_books_cost = (num_books_whales + num_books_fish) * book_price

    # Calculate the total cost of all magazines
    total_magazines_cost = num_magazines * magazine_price

    # Calculate the total cost of all items
    total_cost = total_books_cost + total_magazines_cost
    result = total_cost
    return result

print(solution())