def solution():
    """Donny went to the gas station to gas up his tank. He knows his truck holds 150 liters of fuel. His truck already contained 38 liters. How much change will he get from $350 if each liter of fuel costs $3?"""
    total_fuel_needed = 150 - 38
    cost_of_fuel = total_fuel_needed * 3
    change = 350 - cost_of_fuel
    result = change
    return result

print(solution())