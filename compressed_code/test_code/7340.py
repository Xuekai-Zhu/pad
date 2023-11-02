def solution():
    
    total_sales = 24000
    commission_rate = 0.12
    commission_earned = total_sales * commission_rate
    earnings_saved = (1 - 0.6) * commission_earned
    result = earnings_saved
    return result

print(solution())