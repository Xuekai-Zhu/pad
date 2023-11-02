def solution():
    """Christine makes money by commission rate. She gets a 12% commission on all items she sells. This month, she sold $24,000 worth of items. Sixty percent of all her earnings will be allocated to her personal needs and the rest will be saved. How much did she save this month?"""
    total_sales = 24000
    commission_rate = 0.12
    commission_earned = total_sales * commission_rate
    earnings_saved = (1 - 0.6) * commission_earned
    result = earnings_saved
    return result

print(solution())