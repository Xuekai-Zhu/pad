def solution():
    """Apple and peach trees are planted in the orchard of the Grange Poser farm. The orchard has 30 apple trees that each give 150 kg of apples and 45 peach trees that each produce an average of 65 kg of fruit. What is the total mass of fruit harvested in this orchard?"""
    apple_trees = 30
    apple_yield = 150
    peach_trees = 45
    peach_yield = 65
    total_apples = apple_trees * apple_yield
    total_peaches = peach_trees * peach_yield
    total_fruit = total_apples + total_peaches
    result = total_fruit
    return result

print(solution())