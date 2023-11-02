def solution():
    basic_calculator_price = 8
    scientific_calculator_price = 2 * basic_calculator_price
    graphing_calculator_price = 3 * scientific_calculator_price

    total_cost = basic_calculator_price + scientific_calculator_price + graphing_calculator_price
    change = 100 - total_cost
    result = change
    return result

print(solution())