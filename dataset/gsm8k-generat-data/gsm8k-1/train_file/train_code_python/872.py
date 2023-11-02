def solution():
    """Apple and peach trees are planted in the orchard of the Grange Poser farm. The orchard has 30 apple trees that each give 150 kg of apples and 45 peach trees that each produce an average of 65 kg of fruit. What is the total mass of fruit harvested in this orchard?"""
    apple_trees = 30
    apple_production = 150
    peach_trees = 45
    peach_production = 65
    total_apple_production = apple_trees * apple_production
    total_peach_production = peach_trees * peach_production
    total_fruit_harvested = total_apple_production + total_peach_production
    result = total_fruit_harvested
    
    return result

print(solution())