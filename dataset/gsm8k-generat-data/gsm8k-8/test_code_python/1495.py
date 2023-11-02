def solution():
    # Define the original price of one book
    book_price = 5

    # Define the number of books Sheryll bought
    num_books = 10

    # Define the discount amount per book
    discount = 0.5

    # Calculate the total cost before discount
    total_cost_before_discount = book_price * num_books

    # Calculate the total discount amount
    total_discount_amount = discount * num_books

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - total_discount_amount
    result = total_cost_after_discount
    return result

print(solution())