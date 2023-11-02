def solution():
    num_cat_books = 7
    cat_book_price = 7

    num_system_books = 2
    system_book_price = 7

    num_magazines = 3
    magazine_price = 4

    # Calculate the total cost of all cat books
    total_cat_book_cost = num_cat_books * cat_book_price

    # Calculate the total cost of all system books
    total_system_book_cost = num_system_books * system_book_price

    # Calculate the total cost of all magazines
    total_magazine_cost = num_magazines * magazine_price

    # Calculate the total cost of all items
    total_cost = total_cat_book_cost + total_system_book_cost + total_magazine_cost
    result = total_cost
    return result

print(solution())