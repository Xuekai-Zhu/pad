def solution():
    lamp_cost = 7
    bulb_cost = lamp_cost - 4

    num_lamps = 2
    num_bulbs = 6

    # Calculate the total cost of lamps
    total_lamp_cost = num_lamps * lamp_cost

    # Calculate the total cost of bulbs
    total_bulb_cost = num_bulbs * bulb_cost

    # Calculate the total cost of all items
    total_cost = total_lamp_cost + total_bulb_cost
    result = total_cost
    return result

print(solution())