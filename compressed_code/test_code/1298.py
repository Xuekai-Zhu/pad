def solution():
    
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