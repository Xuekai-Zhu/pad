def solution():
    """James buys a ring for his bride-to-be. The diamond cost $600 and the gold cost $300. He pays a 30% premium for it to be made. How much did he pay?"""
    diamond_cost = 600
    gold_cost = 300
    premium_percent = 30
    premium_amount = (diamond_cost + gold_cost) * (premium_percent / 100)
    total_cost = diamond_cost + gold_cost + premium_amount
    result = total_cost
    return result

print(solution())