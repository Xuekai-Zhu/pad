def solution():
    # John buys 30 cans of soup where he gets 1 free for every 1 he buys
    # So he effectively buys 15 cans and gets 15 free
    cans_bought = 15
    cans_free = 15
    
    # The normal price of 1 can of soup is $0.60
    price_per_can = 0.60
    
    # Calculate the total cost of the cans John buys (without the free cans)
    cost_without_free_cans = cans_bought * price_per_can
    
    # Calculate the total cost of all the cans John gets (including the free ones)
    total_cost = cost_without_free_cans * 2
    
    result = total_cost
    return result

print(solution())