def solution():
    # Calculate the total weight of Jon's textbooks
    jon_textbooks = [2, 8, 5, 9]  # Jon's textbooks weigh 2, 8, 5, and 9 pounds respectively
    jon_total_weight = sum(jon_textbooks)

    # Calculate the weight of Brandon's textbooks
    brandon_total_weight = jon_total_weight / 3  # Jon's textbooks weigh three times as much as Brandon's textbooks

    result = brandon_total_weight
    return result

print(solution())