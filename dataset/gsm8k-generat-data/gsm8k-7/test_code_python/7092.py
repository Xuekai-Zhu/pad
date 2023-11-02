def solution():
    jon_textbook_weights = [2, 8, 5, 9]
    # calculate the total weight of Jon's textbooks
    total_jon_weight = sum(jon_textbook_weights)
    # calculate the weight of each of Brandon's textbooks
    brandon_textbook_weight = total_jon_weight / 3
    result = brandon_textbook_weight
    return result

print(solution())