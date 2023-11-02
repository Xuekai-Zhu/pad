def solution():
    # Calculate the total number of pine cones dropped by all trees
    total_pine_cones = 8 * 200  

    # Calculate the number of pine cones that fall on Alan's roof
    pine_cones_on_roof = total_pine_cones * 0.3  

    # Calculate the total weight of pine cones on Alan's roof
    weight_on_roof = pine_cones_on_roof * 4  

    result = weight_on_roof
    return result

print(solution())