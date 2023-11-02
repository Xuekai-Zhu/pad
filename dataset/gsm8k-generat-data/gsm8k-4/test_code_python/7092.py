def solution():
    """Jon’s textbooks weigh three times as much as Brandon’s textbooks. Jon has four textbooks that weigh two, eight, five and nine pounds respectively. How much do Brandon’s textbooks weigh?"""
    
    # calculate the total weight of Jon's textbooks
    jon_total_weight = 2 + 8 + 5 + 9
    
    # calculate the weight of Brandon's textbooks
    brandon_weight = jon_total_weight / 3
    
    result = brandon_weight
    return result

print(solution())