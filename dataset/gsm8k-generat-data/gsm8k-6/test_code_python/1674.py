def solution():
    silver_weight = 1.5  # weight of silver in ounces
    gold_weight = 2 * silver_weight  # weight of gold in ounces is twice that of silver
    silver_cost = 20 * silver_weight  # cost of silver in dollars
    gold_cost = 50 * 20 * gold_weight  # cost of gold in dollars, 50 times the cost of silver per ounce
    total_cost = silver_cost + gold_cost  # total cost in dollars
    result = total_cost
    return result

print(solution())