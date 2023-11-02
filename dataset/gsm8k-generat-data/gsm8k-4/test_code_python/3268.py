def solution():
    """Romeo buys five bars of chocolate at $5 each and sells these chocolates for a total of $90. If he uses packaging material that costs him $2 for each bar of chocolate, how much profit does he make for all the chocolates he sells?"""
    # Define the cost per bar of chocolate and the price he sells them for
    cost_per_chocolate = 5
    selling_price_per_chocolate = 90 / 5

    # Define the cost of packaging per bar of chocolate
    packaging_cost_per_chocolate = 2

    # Calculate the profit per bar of chocolate
    profit_per_chocolate = selling_price_per_chocolate - cost_per_chocolate - packaging_cost_per_chocolate

    # Calculate the total profit for all the chocolates he sells
    total_profit = profit_per_chocolate * 5

    # return the result
    result = total_profit
    return result

print(solution())