def solution():
    """Martha is grinding a spice paste. She adds 3 tablespoons of ginger, 1 teaspoon of cardamom, 1 teaspoon of mustard, 2 tablespoons of garlic, and four times as much chile powder as mustard. What percentage of the spice paste is ginger, rounded to the nearest integer? (Remember there are three teaspoons per tablespoon.)"""
    ginger_tb = 3
    cardamom_tsp = 1
    mustard_tsp = 1
    garlic_tb = 2
    chile_powder_tsp = 4 * mustard_tsp
    
    total_tsp = (ginger_tb * 3) + cardamom_tsp + mustard_tsp + (garlic_tb * 3) + chile_powder_tsp
    ginger_pct = (ginger_tb * 3 / total_tsp) * 100
    result = round(ginger_pct)
    
    return result

print(solution())