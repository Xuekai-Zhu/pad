def solution():
    """The cost of building a certain house in an area is 100,000 more than the construction cost of each of the houses in the area. But it sells for 1.5 times as much as the other houses, which sell at $320,000 each. How much more profit is made by spending the extra money to build?"""
    other_house_price = 320000
    extra_building_cost = 100000

    # cost to build the special house
    special_house_cost = extra_building_cost + other_house_price

    # selling price of the special house
    special_house_price = 1.5 * other_house_price

    # profit from the special house
    special_house_profit = special_house_price - special_house_cost

    # profit from a regular house
    regular_house_profit = other_house_price * 0.5

    # difference in profit
    difference = special_house_profit - regular_house_profit

    result = difference
    return result

print(solution())