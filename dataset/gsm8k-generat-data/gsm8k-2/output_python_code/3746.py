def solution():
    """A math teacher had $100 to buy three different types of calculators. A basic calculator costs $8. A scientific calculator costs twice the price as the basic while a graphing calculator costs thrice the price as the scientific. How much change did she receive after buying those three different types of calculators?"""
    basic_price = 8
    scientific_price = 2 * basic_price
    graphing_price = 3 * scientific_price
    total_cost = (1 * basic_price) + (1 * scientific_price) + (1 * graphing_price)
    change = 100 - total_cost
    result = change
    return result

print(solution())