def solution():
    """Jon’s textbooks weigh three times as much as Brandon’s textbooks. Jon has four textbooks that weigh two, eight, five and nine pounds respectively. How much do Brandon’s textbooks weigh?"""
    jon_weight = sum([2, 8, 5, 9])
    brandon_weight = jon_weight / 3
    result = brandon_weight
    return result

print(solution())