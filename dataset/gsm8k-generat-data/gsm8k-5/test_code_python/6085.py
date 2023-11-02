def solution():
    # Calculate total amount of water added
    water_added = 8 + (10*2) + 14  # gallons per hour times hours for each rate

    # Calculate total amount of water lost
    water_lost = 8  # gallons lost due to leak in fifth hour

    # Calculate total amount of water in the pool after 5 hours
    water_remaining = water_added - water_lost

    result = water_remaining
    return result

print(solution())