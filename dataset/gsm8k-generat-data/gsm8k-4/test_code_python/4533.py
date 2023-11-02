def solution():
    """Mike decides to develop a plot of land.  He bought 200 acres for $70 per acre.  After development, he sold half of the acreage for $200 per acre.  How much profit did he make?"""
    # Define the initial cost of buying the land
    initial_cost = 200 * 70

    # Define the number of acres sold after development and the price per acre
    sold_acres = 100
    sold_price = 200

    # Calculate the revenue from selling the acres
    revenue = sold_acres * sold_price

    # Calculate the total profit
    profit = revenue - initial_cost

    # return the result
    result = profit
    return result

print(solution())