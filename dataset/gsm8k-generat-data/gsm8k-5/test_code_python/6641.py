def solution():
    previous_weight = 6.4  # The weight of the previous largest spider in ounces
    current_weight = 2.5 * previous_weight  # The weight of the giant spider in ounces
    leg_area = 0.5  # The cross sectional area of each leg in square inches

    # Calculate the force on each leg in ounces
    force_per_leg = current_weight / 8  # The giant spider has 8 legs

    # Calculate the pressure on each leg in ounces per square inch
    pressure_per_leg = force_per_leg / leg_area
    result = pressure_per_leg
    return result

print(solution())