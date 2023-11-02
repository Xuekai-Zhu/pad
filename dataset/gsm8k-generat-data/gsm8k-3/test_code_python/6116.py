def solution():
    """Alan has 8 pine trees in his backyard and each tree drops 200 pine cones. If 30% of the pine cones fall on Alan's roof, and each pine cone weighs 4 ounces, how many ounces of pine cones does Alan have on his roof?"""
    # Define the number of trees and pine cones
    trees = 8
    pine_cones = 200

    # Calculate the total number of pine cones
    total_pine_cones = trees * pine_cones

    # Calculate the number of pine cones that fall on Alan's roof
    roof_pine_cones = total_pine_cones * 0.3

    # Calculate the weight of the pine cones on Alan's roof
    roof_weight = roof_pine_cones * 4

    # Display the weight of the pine cones on Alan's roof
    result = roof_weight
    return result

print(solution())