def solution():
    """Last night, Jim bought a $7 lamp and a bulb which cost $4 less. If he bought 2 lamps and 6 bulbs, how much did Jim pay in all?"""
    lamp_price = 7
    bulb_price = lamp_price - 4
    num_lamps = 2
    num_bulbs = 6
    total_cost = (lamp_price * num_lamps) + (bulb_price * num_bulbs)
    result = total_cost
    return result

print(solution())