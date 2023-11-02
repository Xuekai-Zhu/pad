def solution():
    """A math teacher had $100 to buy three different types of calculators. A basic calculator costs $8. A scientific calculator costs twice the price as the basic while a graphing calculator costs thrice the price as the scientific. How much change did she receive after buying those three different types of calculators?"""
    budget = 100
    basic_calculator_cost = 8
    scientific_calculator_cost = 2 * basic_calculator_cost
    graphing_calculator_cost = 3 * scientific_calculator_cost
    total_cost = basic_calculator_cost + scientific_calculator_cost + graphing_calculator_cost
    change = budget - total_cost
    result = change
    return result

print(solution())