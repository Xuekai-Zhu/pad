def solution():
    # Calculate the profit made by building the more expensive house
    construction_cost = 320000  # cost of constructing each of the other houses in the area
    extra_cost = construction_cost + 100000  # cost of building the more expensive house
    selling_price = 1.5 * 320000  # selling price of each of the other houses in the area
    profit_more_expensive = selling_price - extra_cost  # profit made by building the more expensive house
    result = profit_more_expensive
    return result

print(solution())