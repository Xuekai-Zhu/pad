def solution():
    
    budget = 100
    basic_calculator_cost = 8
    scientific_calculator_cost = 2 * basic_calculator_cost
    graphing_calculator_cost = 3 * scientific_calculator_cost
    total_cost = basic_calculator_cost + scientific_calculator_cost + graphing_calculator_cost
    change = budget - total_cost
    result = change
    return result

print(solution())