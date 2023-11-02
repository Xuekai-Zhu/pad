def solution():
    
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