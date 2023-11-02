def solution():
    """Paul is a chicken trader. One week he had 80 chickens in total to sell at the market. Before he left the farm, he sold his neighbor 12 chickens. At the gate, before the market opens, he got a quick customer and sold another 25 chickens. How many chickens was Paul left with to sell at the market?"""
    total_chickens = 80
    neighbor_chickens = 12
    gate_chickens = 25
    remaining_chickens = total_chickens - neighbor_chickens - gate_chickens
    result = remaining_chickens
    return result

print(solution())