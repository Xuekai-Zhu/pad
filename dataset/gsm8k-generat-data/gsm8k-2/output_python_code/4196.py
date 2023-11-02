def solution():
    """Chantal knits sweaters to sell. Each sweater takes 4 balls of yarn. Each ball of yarn costs $6.
    How much money will Chantal gain in all 28 sweaters if she sells each sweater for $35?"""
    sweater_cost = 4 * 6  # cost of one sweater
    selling_price = 35
    profit_per_sweater = selling_price - sweater_cost
    total_profit = profit_per_sweater * 28
    result = total_profit
    return result

print(solution())