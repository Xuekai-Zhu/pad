def solution():
    total_weeks = 3
    total_chocolates = total_weeks * 2
    local_store_cost = total_chocolates * 3
    promotion_store_cost = total_chocolates * 2
    total_savings = local_store_cost - promotion_store_cost
    result = total_savings
    return result

print(solution())