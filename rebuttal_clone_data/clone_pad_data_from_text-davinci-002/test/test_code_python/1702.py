def solution():
    blueberries_cost = 5.00
    blueberries_ounces = 6
    raspberries_cost = 3.00
    raspberries_ounces = 8
    batches = 4
    ounces_needed = batches * 12
    blueberries_needed = ounces_needed / blueberries_ounces
    raspberries_needed = ounces_needed / raspberries_ounces
    cost_blueberries = blueberries_needed * blueberries_cost
    cost_raspberries = raspberries_needed * raspberries_cost
    savings = cost_blueberries - cost_raspberries
    result = savings
    return result

print(solution())