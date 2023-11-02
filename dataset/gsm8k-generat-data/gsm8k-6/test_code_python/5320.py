def solution():
    # Calculate the total amount of water that enters the bathtub
    total_water_in = 40 * 60 * 9  # rate of dripping in ml/min x minutes in an hour x 9 hours

    # Calculate the total amount of water that evaporates from the bathtub
    total_water_out = 200 * 9  # rate of evaporation in ml/hour x 9 hours

    # Calculate the remaining water in the bathtub
    remaining_water = total_water_in - total_water_out - 12000  # 12 liters = 12000 ml

    result = remaining_water
    return result

print(solution())