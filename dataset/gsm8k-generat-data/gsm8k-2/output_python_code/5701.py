def solution():
    """Donny went to the gas station to gas up his tank. He knows his truck holds 150 liters of fuel. His truck already contained 38 liters. How much change will he get from $350 if each liter of fuel costs $3?"""
    tank_size = 150
    starting_fuel = 38
    fuel_needed = tank_size - starting_fuel
    fuel_cost = 3
    total_cost = fuel_needed * fuel_cost
    change = 350 - total_cost
    result = change
    return result

print(solution())