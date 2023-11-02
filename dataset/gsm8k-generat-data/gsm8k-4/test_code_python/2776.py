def solution():
    """Last night, Jim bought a $7 lamp and a bulb which cost $4 less. If he bought 2 lamps and 6 bulbs, how much did Jim pay in all?"""
    # Define the prices of the lamp and the bulb
    lamp_price = 7
    bulb_price = lamp_price - 4

    # Calculate the total cost of 2 lamps and 6 bulbs
    total_cost = (2 * lamp_price) + (6 * bulb_price)

    result = total_cost
    return result

print(solution())