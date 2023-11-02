def solution():
    """Jon’s textbooks weigh three times as much as Brandon’s textbooks. Jon has four textbooks that weigh two, eight, five and nine pounds respectively. How much do Brandon’s textbooks weigh?"""
    # Calculate the total weight of Jon's textbooks
    jon_total_weight = 2 + 8 + 5 + 9

    # Calculate the weight of Brandon's textbooks
    brandon_weight = jon_total_weight / 3

    # Display the weight of Brandon's textbooks
    result = brandon_weight
    return result

print(solution())