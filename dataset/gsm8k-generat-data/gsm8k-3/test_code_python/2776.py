def solution():
    """Last night, Jim bought a $7 lamp and a bulb which cost $4 less. If he bought 2 lamps and 6 bulbs, how much did Jim pay in all?"""
    # Define the cost of the lamp and bulb
    lamp_cost = 7
    bulb_cost = lamp_cost - 4

    # Define the number of lamps and bulbs purchased
    num_lamps = 2
    num_bulbs = 6

    # Calculate the total cost of the lamps
    lamp_total = num_lamps * lamp_cost

    # Calculate the total cost of the bulbs
    bulb_total = num_bulbs * bulb_cost

    # Calculate the total cost of the purchase
    total_cost = lamp_total + bulb_total

    # Display the total cost
    result = total_cost
    return result

print(solution())