def solution():
    """Kylar went to the store to buy glasses for his new apartment. One glass costs $5, but every second glass costs only 60% of the price. Kylar wants to buy 16 glasses. How much does he need to pay for them?"""
    glasses_count = 16
    full_price_glass = 5
    discount_glass_price = 0.6 * full_price_glass
    total_cost = ((glasses_count + 1) // 2) * (full_price_glass + discount_glass_price)
    result = total_cost
    return result

print(solution())