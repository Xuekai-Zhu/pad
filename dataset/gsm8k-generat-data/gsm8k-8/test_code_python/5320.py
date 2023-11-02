def solution():
    # Calculate the total amount of water that flowed into the bathtub
    water_in = 40 * 60 * 9  # ml/min * min/hour * hours

    # Calculate the amount of water that evaporated
    water_out = 200 * 9  # ml/hour * hours

    # Calculate the amount of water that was dumped out
    water_dumped = 12000  # ml

    # Calculate the remaining amount of water in the bathtub
    water_remaining = water_in - water_out - water_dumped
    result = water_remaining
    return result

print(solution())