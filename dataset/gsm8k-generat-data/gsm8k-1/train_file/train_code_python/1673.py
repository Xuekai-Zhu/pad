def solution():
    """John buys 1.5 ounces of silver and twice as much gold. The silver costs $20 per ounce. The gold is 50 times more expensive per ounce. How much does he spend on everything?"""
    silver_weight = 1.5
    silver_cost_per_ounce = 20
    gold_weight = silver_weight * 2
    gold_cost_per_ounce = silver_cost_per_ounce * 50
    total_cost = (silver_weight * silver_cost_per_ounce) + (gold_weight * gold_cost_per_ounce)
    result = total_cost
    return result

print(solution())