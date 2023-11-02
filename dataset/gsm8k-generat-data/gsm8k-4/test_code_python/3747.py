def solution():
    """A math teacher had $100 to buy three different types of calculators. A basic calculator costs $8. A scientific calculator costs twice the price as the basic while a graphing calculator costs thrice the price as the scientific. How much change did she receive after buying those three different types of calculators?"""
    # Define the prices of the calculators
    basic_price = 8
    scientific_price = 2 * basic_price
    graphing_price = 3 * scientific_price

    # Calculate the total cost of all three types of calculators
    total_cost = basic_price + scientific_price + graphing_price

    # Calculate the change she received
    change = 100 - total_cost

    # Return the result
    result = change
    return result

print(solution())