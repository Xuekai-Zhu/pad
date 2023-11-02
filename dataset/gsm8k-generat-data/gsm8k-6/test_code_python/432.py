def solution():
    # Calculate the total profit and cost of making the books
    total_profit = 120
    cost_per_book = 5
    profit_per_book = 20 - cost_per_book
    books_sold = total_profit / profit_per_book  # total number of books sold
    customers = books_sold / 2  # each customer buys 2 books
    result = customers
    return result

print(solution())