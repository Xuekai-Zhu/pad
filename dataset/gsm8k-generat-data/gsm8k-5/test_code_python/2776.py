def solution():
    lamp_cost = 7  # Jim bought a $7 lamp
    bulb_cost = lamp_cost - 4  # The bulb costs $4 less than the lamp
    num_lamps = 2  # Jim bought 2 lamps
    num_bulbs = 6  # Jim bought 6 bulbs

    # Calculate the total cost of the lamps
    total_lamp_cost = num_lamps * lamp_cost

    # Calculate the total cost of the bulbs
    total_bulb_cost = num_bulbs * bulb_cost

    # Calculate the overall cost
    total_cost = total_lamp_cost + total_bulb_cost
    result = total_cost
    return result

print(solution())