def solution():
    """On a construction site, the Laker cement factory provided 500 bags of cement sold to Mr. Zander at $10 per bag. 
    Mr. Zander also received twenty lorries of construction sand, each carrying 10 tons of sand, sold at $40 per ton. 
    How much money did Mr. Zander pay for these construction materials?"""
    cement_bags = 500
    cement_price = 10
    sand_lorries = 20
    sand_tons_per_lorry = 10
    sand_price_per_ton = 40
    total_cement_cost = cement_bags * cement_price
    total_sand_cost = sand_lorries * sand_tons_per_lorry * sand_price_per_ton
    total_cost = total_cement_cost + total_sand_cost
    result = total_cost
    return result

print(solution())