def solution():
    # Calculate the total cost of the calculators
    basic_calculator_cost = 8
    scientific_calculator_cost = 2 * basic_calculator_cost
    graphing_calculator_cost = 3 * scientific_calculator_cost
    total_cost = basic_calculator_cost + scientific_calculator_cost + graphing_calculator_cost

    # Calculate the amount of change received
    change = 100 - total_cost
    result = change
    return result

print(solution())