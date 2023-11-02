def solution():
    """Steve's new book sells 1,000,000 copies. He got an advance to pay for 100,000 copies. He gets $2 for each copy of the book sold. His agent takes 10% of that. How much money did he keep not counting the money from the advance?"""
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