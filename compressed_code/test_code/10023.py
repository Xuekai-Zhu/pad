def solution():
    
    total_copies = 1000000
    advance_copies = 100000
    sale_copies = total_copies - advance_copies
    sale_price = 2
    agent_percentage = 10
    agent_cut = (sale_price * agent_percentage) / 100
    earnings_per_book = sale_price - agent_cut
    total_earnings = earnings_per_book * sale_copies
    result = total_earnings
    
    return result

print(solution())