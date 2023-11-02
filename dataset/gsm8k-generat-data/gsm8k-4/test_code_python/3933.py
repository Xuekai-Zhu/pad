def solution():
    """Burt spent $2.00 on a packet of basil seeds and $8.00 on potting soil. The packet of seeds yielded 20 basil plants. He sells each basil plant for $5.00 at the local farmer's market. What is the net profit from his basil plants?"""
    # Define the cost of the seeds and the soil
    seed_cost = 2.0
    soil_cost = 8.0

    # Calculate the number of basil plants produced
    basil_plants = 20

    # Calculate the total revenue from selling the basil plants
    revenue = basil_plants * 5.0

    # Calculate the total cost of producing the basil plants
    cost = seed_cost + soil_cost

    # Calculate the net profit
    net_profit = revenue - cost

    # Return the result
    result = net_profit
    return result

print(solution())