def solution():
    """A farmer is growing corn. For every 4 seeds he plants, he gets one ear of corn, that he can sell for $.1. It costs $.5 for a bag with 100 seeds. If he makes $40 in profit, how many ears did he sell?"""
    seeds_per_bag = 100
    cost_per_bag = 0.5
    price_per_ear = 0.1
    
    # Calculate profit per ear
    profit_per_ear = price_per_ear - (cost_per_bag / seeds_per_bag) * 4
    
    # Calculate the number of ears sold
    total_profit = 40
    ears_sold = total_profit / profit_per_ear
    
    result = ears_sold
    return result

print(solution())