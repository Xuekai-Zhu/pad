def solution():
    """Paul is a chicken trader. One week he had 80 chickens in total to sell at the market. Before he left the farm, he sold his neighbor 12 chickens. At the gate, before the market opens, he got a quick customer and sold another 25 chickens. How many chickens was Paul left with to sell at the market?"""
    total_chickens = 80
    chickens_sold_neighbor = 12
    chickens_sold_gate = 25
    chickens_left = total_chickens - chickens_sold_neighbor - chickens_sold_gate
    result = chickens_left
    return result

print(solution())