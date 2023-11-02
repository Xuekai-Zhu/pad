def solution():
    # Let x be the number of tent stakes bought
    x = 0
    
    # Number of packets of drink mix bought is 3 times the number of tent stakes
    drink_mix = 3 * x
    
    # Number of bottles of water bought is 2 more than the number of tent stakes
    water = x + 2
    
    # Total items bought is 22
    total_items = x + drink_mix + water
    
    # Solve for x
    x = (22 - water - drink_mix) / 2
    
    result = x
    return result

print(solution())