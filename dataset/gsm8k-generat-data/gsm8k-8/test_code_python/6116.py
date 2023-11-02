def solution():
    # Calculate the total number of pine cones
    total_pine_cones = 8 * 200

    # Calculate the number of pine cones that will fall on the roof
    roof_pine_cones = 0.3 * total_pine_cones

    # Calculate the total weight of the pine cones on the roof
    roof_weight = roof_pine_cones * 4

    result = roof_weight
    return result

print(solution())