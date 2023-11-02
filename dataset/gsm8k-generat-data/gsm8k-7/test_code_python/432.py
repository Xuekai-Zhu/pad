def solution():
    profit = 120
    earnings_per_book = 20
    cost_per_book = 5
    num_books_per_customer = 2

    # Calculate the total earnings from book sales
    total_earnings = profit + (cost_per_book * num_books_per_customer)

    # Calculate the number of books sold
    num_books_sold = total_earnings / earnings_per_book

    # Calculate the number of customers who bought books
    num_customers = num_books_sold / num_books_per_customer
    result = num_customers
    return result

print(solution())