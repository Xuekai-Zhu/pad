def solution():
    num_english_books = 35
    english_book_price = 7.5

    num_geography_books = 35
    geography_book_price = 10.5

    # Calculate the total cost of all English books
    total_english_cost = num_english_books * english_book_price

    # Calculate the total cost of all geography books
    total_geography_cost = num_geography_books * geography_book_price

    # Calculate the total cost of the order
    total_order_cost = total_english_cost + total_geography_cost
    result = total_order_cost
    return result

print(solution())