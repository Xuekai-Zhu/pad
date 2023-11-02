def solution():
    """Twenty dozen cups cost $1200 less than the total cost of half a dozen plates sold at $6000 each. Calculate the total cost of buying each cup."""
    dozen_cups = 20
    total_cups = dozen_cups * 12
    plate_price = 6000 / 2
    total_cost_plates = plate_price * 6
    cost_per_cup = (total_cost_plates - 1200) / total_cups
    result = cost_per_cup
    return result

print(solution())