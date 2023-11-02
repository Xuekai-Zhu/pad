def solution():
    """Paul is a chicken trader. One week he had 80 chickens in total to sell at the market. Before he left the farm, he sold his neighbor 12 chickens. At the gate, before the market opens, he got a quick customer and sold another 25 chickens. How many chickens was Paul left with to sell at the market?"""
    # Define the initial number of chickens
    chickens = 80

    # Subtract the chickens sold to the neighbor
    chickens -= 12

    # Subtract the chickens sold before the market
    chickens -= 25

    # Display the number of chickens left to sell at the market
    result = chickens
    return result

print(solution())