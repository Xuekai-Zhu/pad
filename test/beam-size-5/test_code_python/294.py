def solution():
    
    opening_bid = 200
    bid_1 = 50
    bid_2 = 50
    bid_3 = 3
    total_bids = opening_bid + (bid_1 * bid_2) + (bid_3 * bid_3)
    total_cost = total_bids * cost_1
    result = total_cost
    return result

print(solution())