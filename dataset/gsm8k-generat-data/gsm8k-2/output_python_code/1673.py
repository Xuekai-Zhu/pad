def solution():
    """John buys 1.5 ounces of silver and twice as much gold. The silver costs $20 per ounce. The gold is 50 times more expensive per ounce. How much does he spend on everything?"""
    silver_ounces = 1.5
    gold_ounces = 2 * silver_ounces
    silver_cost = 20
    gold_cost = 50 * silver_cost
    total_silver_cost = silver_ounces * silver_cost
    total_gold_cost = gold_ounces * gold_cost
    total_cost = total_silver_cost + total_gold_cost
    result = total_cost
    return result

print(solution())