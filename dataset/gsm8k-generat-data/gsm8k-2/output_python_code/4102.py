def solution():
    """Abraham is buying some toiletries and creates a budget of $60 for his shopping. He buys 4 shower gels for $4 each, a tube of toothpaste for $3, and a box of laundry detergent. If he has $30 remaining in his budget, how much money, in dollars, did Abraham spend on the box of laundry detergent?"""
    budget = 60
    shower_gel_price = 4
    toothpaste_price = 3
    remaining_budget = 30
    shower_gel_total_price = shower_gel_price * 4
    total_spent = budget - remaining_budget - shower_gel_total_price - toothpaste_price
    detergent_price = total_spent
    result = detergent_price
    return result

print(solution())