def solution():
    # Calculate the weight of the giant spider
    weight_giant_spider = 2.5 * 6.4  # the giant spider weighs 2.5 times the previous largest spider

    # Calculate the total cross-sectional area of all the legs
    total_leg_area = 8 * 0.5  # the giant spider has 8 legs, each with a cross-sectional area of 0.5 square inches

    # Calculate the pressure on each leg in ounces per square inch
    pressure_per_leg = weight_giant_spider / total_leg_area

    result = pressure_per_leg
    return result

print(solution())