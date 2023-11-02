def solution():
    """Mark hires a singer for 3 hours at $15 an hour. He then tips the singer 20%. How much did he pay?"""
    hours = 3
    rate_per_hour = 15
    tip_percent = 20
    total_cost = hours * rate_per_hour
    tip_amount = total_cost * (tip_percent / 100)
    final_cost = total_cost + tip_amount
    result = final_cost
    return result

print(solution())