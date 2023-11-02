def solution():
    """Romeo buys five bars of chocolate at $5 each and sells these chocolates for a total of $90. If he uses packaging material that costs him $2 for each bar of chocolate, how much profit does he make for all the chocolates he sells?"""
    # Define the cost and selling price of each chocolate bar
    COST_PER_BAR = 5
    SELLING_PRICE_PER_BAR = 18

    # Define the cost of packaging per bar
    PACKAGING_COST_PER_BAR = 2

    # Calculate the total cost of the chocolates
    total_cost = 5 * (COST_PER_BAR + PACKAGING_COST_PER_BAR)

    # Calculate the profit from selling the chocolates
    profit = 90 - total_cost

    # Display the profit
    result = profit
    return result

print(solution())