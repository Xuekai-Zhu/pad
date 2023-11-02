def solution():
    """Julie is making caesar salad for a family picnic. At the market, she spends $8 on green lettuce and $6 on red lettuce. If each type of lettuce costs $2 per pound, how many total pounds of lettuce did she buy?"""
    green_lettuce_cost = 8
    red_lettuce_cost = 6
    
    # Calculate pounds of each type of lettuce
    green_lettuce_pounds = green_lettuce_cost / 2
    red_lettuce_pounds = red_lettuce_cost / 2
    
    # Calculate total pounds of lettuce
    total_pounds = green_lettuce_pounds + red_lettuce_pounds
    
    result = total_pounds
    return result

print(solution())