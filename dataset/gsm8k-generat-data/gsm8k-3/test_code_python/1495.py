def solution():
    """In a bookstore, a book costs $5. When Sheryll bought 10 books, she was given a discount of $0.5 each. How much did Sheryll pay in all?"""
    # Define the cost of each book and the discount amount
    BOOK_PRICE = 5
    DISCOUNT = 0.5

    # Define the number of books purchased
    num_books = 10

    # Calculate the total cost of the books without the discount
    total_cost = num_books * BOOK_PRICE

    # Calculate the discount amount
    discount_amount = num_books * DISCOUNT

    # Calculate the total cost with the discount
    total_cost_with_discount = total_cost - discount_amount

    # Display the total cost with the discount
    result = total_cost_with_discount
    return result

print(solution())