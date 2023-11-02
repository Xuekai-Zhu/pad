def solution():
    base_house_cost = 320000
    extra_cost = 100000
    sell_price_ratio = 1.5

    # Calculate the cost of building the special house
    special_house_cost = base_house_cost + extra_cost

    # Calculate the selling price of the special house
    special_house_sell_price = sell_price_ratio * base_house_cost

    # Calculate the profit made by selling the special house
    special_house_profit = special_house_sell_price - special_house_cost

    # Calculate the profit made by building the special house instead of a regular house
    extra_profit = special_house_profit - (sell_price_ratio - 1) * base_house_cost

    result = extra_profit
    return result

print(solution())