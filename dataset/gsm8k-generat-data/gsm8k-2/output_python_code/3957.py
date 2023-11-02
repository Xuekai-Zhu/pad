def solution():
    """It's Mother's day, so mothers get a 10% discount on the department store. Mothers who have 3 children or more can get an additional 4% off the discounted price. If Mrs. Brown has 4 children and wants to buy a pair of shoes that costs $125, how much will she pay?"""
    original_price = 125
    discount_1 = 0.10
    discount_2 = 0.04
    num_children = 4
    
    # First discount
    discounted_price = original_price * (1 - discount_1)
    
    # Additional discount for mothers with 3 or more children
    if num_children >= 3:
        discounted_price *= (1 - discount_2)
        
    result = discounted_price
    return result

print(solution())