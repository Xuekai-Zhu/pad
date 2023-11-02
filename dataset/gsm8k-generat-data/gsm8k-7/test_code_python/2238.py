def solution():
    total_chickens = 80
    neighbor_chickens = 12
    pre_market_chickens = 25

    # Subtract the chickens sold to the neighbor and pre-market customer
    chickens_left = total_chickens - neighbor_chickens - pre_market_chickens
    result = chickens_left
    return result

print(solution())