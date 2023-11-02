def solution():
    """John reels in 3 crab baskets a week. Each basket holds 4 crabs. He collects crabs twice a week. Each crab sells for $3. How much money does he make?"""
    baskets_per_week = 3
    crabs_per_basket = 4
    crabs_per_week = baskets_per_week * crabs_per_basket
    times_per_week = 2
    total_crabs = crabs_per_week * times_per_week
    price_per_crab = 3
    total_money = total_crabs * price_per_crab
    result = total_money
    return result

print(solution())