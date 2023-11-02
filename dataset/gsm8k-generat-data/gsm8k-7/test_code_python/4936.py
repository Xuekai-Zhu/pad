def solution():
    five_liters = 5
    three_liters = 3
    six_liters = 6

    # Fill the 5-liter bucket
    current_amount = five_liters

    # Pour into the 3-liter bucket as much as possible
    current_amount -= three_liters

    # If there's still some water left in the 5-liter bucket, pour it into the 6-liter bucket
    if current_amount > 0:
        current_amount += six_liters - current_amount
    else:
        current_amount = six_liters

    # Calculate how much more water can fit into the 6-liter bucket
    remaining_space = six_liters - current_amount
    result = remaining_space
    return result

print(solution())