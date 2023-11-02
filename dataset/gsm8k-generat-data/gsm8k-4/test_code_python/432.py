def solution():
    """Tina is getting $20 for each book she sells. If she realizes a $120 profit on her sales, how many people have she sold the books to if each book costs $5 to make and every customer buys 2 at a time?"""
    # Define the profit and the cost of making each book
    profit = 120
    cost_per_book = 5

    # Calculate the number of books sold
    total_profit = profit + (cost_per_book * 2 * x)
    x = total_profit / 20

    # Calculate the number of customers
    customers = x / 2

    # Return the result
    result = customers
    return result

print(solution())