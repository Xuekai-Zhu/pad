def solution():
    num_cement_bags = 500
    cement_price = 10
    num_sand_lorries = 20
    sand_price_per_ton = 40
    sand_tons_per_lorry = 10

    # Calculate the total cost of all cement bags
    total_cement_cost = num_cement_bags * cement_price

    # Calculate the total cost of all sand lorries
    total_sand_cost = num_sand_lorries * sand_tons_per_lorry * sand_price_per_ton

    # Calculate the total cost of all construction materials
    total_cost = total_cement_cost + total_sand_cost
    result = total_cost
    return result

print(solution())