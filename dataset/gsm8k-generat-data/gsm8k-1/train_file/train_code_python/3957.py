def solution():
    """It's Mother's day, so mothers get a 10% discount on the department store. Mothers who have 3 children or more can get an additional 4% off the discounted price. If Mrs. Brown has 4 children and wants to buy a pair of shoes that costs $125, how much will she pay?"""
    original_price = 125
    discount_percent = 10
    discounted_price = original_price * (1 - (discount_percent / 100))
    if children >= 3:
        additional_discount_percent = 4
        discounted_price = discounted_price * (1 - (additional_discount_percent / 100))
    result = discounted_price
    
    return result

print(solution())