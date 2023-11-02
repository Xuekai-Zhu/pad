def solution():
    book_price = 5
    num_books = 10

    # Calculate the total cost of all books before discount
    total_cost_before_discount = book_price * num_books

    # Calculate the total discount received
    discount_per_book = 0.5
    total_discount = discount_per_book * num_books

    # Calculate the total cost of all books after discount
    total_cost_after_discount = total_cost_before_discount - total_discount

    result = total_cost_after_discount
    return result

print(solution())