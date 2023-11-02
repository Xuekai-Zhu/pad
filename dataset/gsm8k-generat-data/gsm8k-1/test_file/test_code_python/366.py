def solution():
    """A hand-painted wallpaper costs $400 at the market. A DIY will save 20% after considering the materials cost. If Ethan made his own hand-painted wallpaper, how much was the total cost?"""
    market_cost = 400
    savings_percent = 20
    material_cost = market_cost / (100 + savings_percent) * savings_percent
    total_cost = market_cost - material_cost
    result = total_cost
    return result

print(solution())