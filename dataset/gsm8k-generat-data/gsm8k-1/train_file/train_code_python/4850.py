def solution():
    """Stephanie is moving into a new apartment. She needs to figure out how many pieces of silverware she should purchase. 
    She needs spoons, butter knives, steak knives, and forks. For herself she figures 5 of each would be sufficient. But in case 
    she has guests, she wants to have 10 extra pieces of each type. Then she realizes that if everything is clean at the same 
    time, that she will have too many of everything and not enough room to fit them in her kitchen silverware drawer. So she 
    decides to purchase 4 fewer spoons, 4 fewer butter knives, 5 fewer steak knives, and 3 fewer forks. How many pieces total 
    of all the silverware is Stephanie going to buy?"""
    
    total_silverware = 4 * (5 + 10) * 4
    total_silverware -= 4 * 5
    total_silverware -= 4 * (5 + 10)
    total_silverware -= 5 * (5 + 10 - 5)
    total_silverware -= 3 * (5 + 10 - 3)
    result = total_silverware
    return result

print(solution())