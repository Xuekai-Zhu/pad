def solution():
    # Calculate the total cost of making the books
    book_cost = 5 * 2  # $10 for 2 books

    # Calculate the total revenue from selling the books
    total_revenue = 120 + book_cost

    # Calculate the number of books Tina sold
    num_books = total_revenue / 20  # $20 per book

    # Calculate the number of customers Tina sold to
    num_customers = num_books / 2  # 2 books per customer

    result = num_customers
    return result

print(solution())