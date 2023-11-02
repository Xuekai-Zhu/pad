def solution():
    """Donny went to the gas station to gas up his tank. He knows his truck holds 150 liters of fuel. His truck already contained 38 liters. How much change will he get from $350 if each liter of fuel costs $3?"""
    # Define the amount of fuel Donny needs to fill up his tank
    fuel_needed = 150 - 38

    # Calculate the cost of the fuel Donny needs
    fuel_cost = fuel_needed * 3

    # Calculate the change Donny will receive using the given amount
    change = 350 - fuel_cost

    # return the result
    result = change
    return result

print(solution())