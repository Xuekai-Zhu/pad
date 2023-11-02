def solution():
    
    total_copies = 1000000
    advance_copies = 100000
    sold_copies = total_copies - advance_copies
    price_per_copy = 2
    agent_cut = 0.1
    earnings_per_copy = price_per_copy * (1 - agent_cut)
    total_earnings = sold_copies * earnings_per_copy
    result = total_earnings
    return result

print(solution())