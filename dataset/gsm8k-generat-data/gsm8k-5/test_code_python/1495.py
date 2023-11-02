def solution():
    book_price = 5  # Each book costs $5
    discount = 0.5  # Sheryll received a discount of $0.5 per book
    num_books = 10  # Sheryll bought 10 books

    # Calculate the total cost of the books before the discount
    total_cost_before_discount = book_price * num_books

    # Calculate the total discount Sheryll received
    total_discount = discount * num_books

    # Calculate the total cost of the books after the discount
    total_cost_after_discount = total_cost_before_discount - total_discount

    result = total_cost_after_discount
    return result

print(solution())