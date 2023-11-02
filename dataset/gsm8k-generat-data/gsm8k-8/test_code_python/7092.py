def solution():
    # Calculate the total weight of Jon's textbooks
    jon_textbooks_weight = 2 + 8 + 5 + 9
    # Calculate the ratio of Jon's textbook weight to Brandon's textbook weight
    jon_to_brandon_ratio = 3
    # Solve for the weight of Brandon's textbooks using the ratio and Jon's textbooks weight
    brandon_textbooks_weight = jon_textbooks_weight / (jon_to_brandon_ratio + 1)
    result = brandon_textbooks_weight
    return result

print(solution())