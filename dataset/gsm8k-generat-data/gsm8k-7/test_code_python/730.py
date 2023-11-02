def solution():
    num_books_per_month = 3
    book_price = 20
    num_months = 12
    selling_price = 500

    # Calculate the total cost of all books purchased
    total_purchase_cost = num_books_per_month * book_price * num_months

    # Calculate the loss from selling the books back
    loss = total_purchase_cost - selling_price
    result = loss
    return result

print(solution())