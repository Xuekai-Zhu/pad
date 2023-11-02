def solution():
    weight_limit = 20 * 16  # Weight limit in ounces
    plate_weight = 10  # Weight of one plate in ounces
    num_plates = 38

    # Calculate the initial weight of the box
    initial_weight = plate_weight * num_plates

    # Check if the initial weight is under the weight limit
    if initial_weight <= weight_limit:
        return 0  # No plates need to be removed

    # Loop through removing one plate at a time until the weight is under the limit
    while initial_weight > weight_limit:
        num_plates -= 1
        initial_weight = plate_weight * num_plates

    result = 38 - num_plates
    return result

print(solution())