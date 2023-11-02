def solution():
    original_price = 0
    
    # Check if the 20% discount applies
    if 18 > 15:
        discounted_price = 500  # Paid price after 20% discount

        # Calculate the original price using the discounted price
        original_price = discounted_price / 0.8
    else:
        original_price = 500  # No discount applied, paid price is the original price
        
    result = original_price
    return result

print(solution())