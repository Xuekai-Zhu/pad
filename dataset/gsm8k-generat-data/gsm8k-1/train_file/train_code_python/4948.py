def solution():
    """Françoise sells pots of lily of the valley to fund humanitarian work. She buys them at €12 each and sells them at a 25% higher cost. How much will she give back to the association by selling 150 pots of lily of the valley?"""
    cost_per_pot = 12
    selling_price = cost_per_pot * 1.25
    total_profit = selling_price - cost_per_pot
    total_fund_raised = total_profit * 150
    result = total_fund_raised
    return result

print(solution())