def solution():
    """Burt spent $2.00 on a packet of basil seeds and $8.00 on potting soil.  The packet of seeds yielded 20 basil plants.  He sells each basil plant for $5.00 at the local farmer's market.  What is the net profit from his basil plants?"""
    # Define the cost of the seeds and soil, and the selling price per plant
    SEEDS_COST = 2.00
    SOIL_COST = 8.00
    SELLING_PRICE = 5.00

    # Calculate the total cost of Burt's supplies
    total_cost = SEEDS_COST + SOIL_COST

    # Calculate the total revenue from selling the basil plants
    total_revenue = 20 * SELLING_PRICE

    # Calculate the net profit
    net_profit = total_revenue - total_cost

    # Display the net profit
    result = net_profit
    return result

print(solution())