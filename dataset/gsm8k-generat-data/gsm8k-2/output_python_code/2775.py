def solution():
    """Last night, Jim bought a $7 lamp and a bulb which cost $4 less. If he bought 2 lamps and 6 bulbs, how much did Jim pay in all?"""
    lamp_price = 7
    bulb_price = lamp_price - 4
    total_lamp_cost = 2 * lamp_price
    total_bulb_cost = 6 * bulb_price
    total_cost = total_lamp_cost + total_bulb_cost
    result = total_cost
    return result

print(solution())