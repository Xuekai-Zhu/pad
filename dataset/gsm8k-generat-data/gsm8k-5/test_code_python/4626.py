def solution():
    other_cost = 320000 # cost of other houses in the area
    extra_cost = other_cost + 100000 # cost of building this certain house
    selling_price = 1.5 * other_cost # selling price of certain house

    # Calculate the profit from building the certain house
    profit = selling_price - extra_cost

    result = profit
    return result

print(solution())