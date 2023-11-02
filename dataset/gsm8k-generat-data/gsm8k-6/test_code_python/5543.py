def solution():
    # Calculate the total cost of the 30 cans of soup
    normal_price = 0.60  # cost of one can of soup
    cans_bought = 30  
    cost = (cans_bought // 2) * normal_price  # buy 1 get 1 free, so we only pay for half the cans
    result = cost
    return result

print(solution())