def solution():
    bags_of_cement = 500
    price_per_bag = 10
    lorries_of_sand = 20
    tons_per_lorry = 10
    price_per_ton = 40
    total_cost = (bags_of_cement * price_per_bag) + (lorries_of_sand * tons_per_lorry * price_per_ton)
    result = total_cost
    return result

print(solution())