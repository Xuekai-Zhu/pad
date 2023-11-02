def solution():
    initial_amount = 150
    remaining_amount = 25

    # Calculate the amount spent on hockey skates
    skates_cost = initial_amount / 2

    # Calculate the amount spent on hockey pads
    pads_cost = initial_amount - skates_cost - remaining_amount

    result = pads_cost
    return result

print(solution())