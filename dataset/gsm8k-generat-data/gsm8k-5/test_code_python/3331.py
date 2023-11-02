def solution():
    weight_limit = 20 * 16  # The weight limit for each box is 20 pounds, and there are 16 ounces in one pound
    plate_weight = 10 / 16  # Each plate weighs 10 ounces, and there are 16 ounces in one pound

    # Calculate the initial weight of the box with 38 plates
    initial_weight = 38 * plate_weight

    # Calculate the weight after removing one plate
    weight_after_one_plate = (38 - 1) * plate_weight

    # Calculate the weight after removing two plates
    weight_after_two_plates = (38 - 2) * plate_weight

    # Continue removing plates until the weight is less than or equal to the weight limit
    while initial_weight > weight_limit:
        initial_weight = initial_weight - plate_weight
        if initial_weight <= weight_limit:
            break
        initial_weight = initial_weight - plate_weight
        if initial_weight <= weight_limit:
            break

    # Calculate the number of plates removed
    plates_removed = 38 - int(initial_weight / plate_weight)
    result = plates_removed
    return result

print(solution())