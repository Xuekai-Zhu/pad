def solution():
    bottles_per_month = 15
    cost_per_bottle = 3
    refund_per_bottle = 0.1
    bottles_recycled_per_year = 12 * bottles_per_month
    total_refund = bottles_recycled_per_year * refund_per_bottle
    total_cost = bottles_recycled_per_year * cost_per_bottle
    money_left = total_refund - total_cost
    bottles_bought = money_left / cost_per_bottle
    result = bottles_bought
    
    return result

print(solution())