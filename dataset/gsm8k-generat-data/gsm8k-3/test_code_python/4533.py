def solution():
    """Mike decides to develop a plot of land.  He bought 200 acres for $70 per acre.  After development, he sold half of the acreage for $200 per acre.  How much profit did he make?"""
    # Define the number of acres bought and the price per acre
    ACRES_BOUGHT = 200
    PRICE_PER_ACRE = 70

    # Calculate the total cost of the land
    total_cost = ACRES_BOUGHT * PRICE_PER_ACRE

    # Calculate the revenue from selling half of the land
    acres_sold = ACRES_BOUGHT / 2
    revenue = acres_sold * 200

    # Calculate the profit
    profit = revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())