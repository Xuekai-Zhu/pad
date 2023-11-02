def solution():
    """Françoise sells pots of lily of the valley to fund humanitarian work. She buys them at €12 each and sells them at a 25% higher cost. How much will she give back to the association by selling 150 pots of lily of the valley?"""
    buying_price = 12
    selling_price = buying_price * 1.25
    num_pots = 150
    profit_per_pot = selling_price - buying_price
    total_profit = profit_per_pot * num_pots
    result = total_profit
    return result

print(solution())