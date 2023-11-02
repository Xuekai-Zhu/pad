def solution():
    
    original_price = 500
    week_reduction = 0.05 * original_price
    week_price = original_price - week_reduction
    month_reduction = 0.04 * week_price
    final_price = week_price - month_reduction
    total_reduction = original_price - final_price
    result = total_reduction
    return result

print(solution())