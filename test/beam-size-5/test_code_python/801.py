def solution():
    
    diamond_cost = 600
    gold_cost = 300
    total_cost = diamond_cost + gold_cost
    premium_percent = 30
    premium_amount = total_cost * (premium_percent / 100)
    total_cost_with_premium = total_cost + premium_amount
    result = total_cost_with_premium
    return result

print(solution())