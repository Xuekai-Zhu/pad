def solution():
    coupe_price = 30000
    suv_price = 2 * coupe_price
    total_sales = coupe_price + suv_price
    commission_rate = 0.02
    commission_earned = total_sales * commission_rate
    result = commission_earned
    return result

print(solution())