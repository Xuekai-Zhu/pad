def solution():
    """Christine makes money by commission rate. She gets a 12% commission on all items she sells. This month, she sold $24000 worth of items. Sixty percent of all her earning will be allocated to her personal needs and the rest will be saved. How much did she save this month?"""
    sales = 24000
    commission_rate = 0.12
    commission_earned = sales * commission_rate
    personal_needs = 0.6 * commission_earned
    savings = commission_earned - personal_needs
    result = savings
    return result

print(solution())