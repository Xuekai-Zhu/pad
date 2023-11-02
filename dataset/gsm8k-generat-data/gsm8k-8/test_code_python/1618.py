def solution():
    # Calculate the price of the cheaper pair of shoes
    if 40 < 60:
        cheaper_pair_price = 40
    else:
        cheaper_pair_price = 60
    
    # Calculate the price of the more expensive pair of shoes
    more_expensive_pair_price = 100 - cheaper_pair_price
    
    # Calculate the total price before the extra discount
    total_price_before_discount = cheaper_pair_price + more_expensive_pair_price
    
    # Calculate the amount of the extra discount
    extra_discount_amount = 0.25 * total_price_before_discount
    
    # Calculate the total price after the extra discount
    total_price_after_extra_discount = total_price_before_discount - extra_discount_amount
    
    result = total_price_after_extra_discount
    return result

print(solution())