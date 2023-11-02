def solution():
    discounted_price = 480  # Lyra paid $480 for the shoes
    discount_percentage = 20  # The shoes were discounted by 20%
    
    # Calculate the original price of the shoes before the discount
    original_price = discounted_price / (1 - (discount_percentage / 100))
    result = original_price
    return result

print(solution())