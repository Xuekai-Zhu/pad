def solution():
    """Paul is a chicken trader. One week he had 80 chickens in total to sell at the market. Before he left the farm, he sold his neighbor 12 chickens. At the gate, before the market opens, he got a quick customer and sold another 25 chickens. How many chickens was Paul left with to sell at the market?"""
    # Define the initial number of chickens
    initial_chickens = 80

    # Subtract the number of chickens he sold to his neighbor
    chickens_after_neighbor = initial_chickens - 12

    # Subtract the number of chickens he sold to the quick customer
    chickens_at_market = chickens_after_neighbor - 25

    # Return the result
    result = chickens_at_market
    return result

print(solution())