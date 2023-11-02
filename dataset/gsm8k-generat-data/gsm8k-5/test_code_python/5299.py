def solution():
    total_customers = 1000  # Dianne has 1000 customers
    return_percent = 0.37  # 37% of customers return their books
    book_cost = 15  # Each book costs $15

    # Calculate the total number of returned books
    returned_books = total_customers * return_percent

    # Calculate the total amount of money Dianne made from book sales
    total_sales = total_customers * book_cost

    # Calculate the total amount of money Dianne keeps after subtracting returns
    sales_after_returns = total_sales - (returned_books * book_cost)
    result = sales_after_returns
    return result

print(solution())