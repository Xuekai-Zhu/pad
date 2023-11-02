def solution():
    max_price = 1000  # The maximum amount Martin decided to spend
    discount = 0.2  # The discount offered by the sales clerk
    original_price = max_price + 100  # The original price of the television before the discount
    
    # Calculate the final price after the discount
    final_price = original_price - (original_price * discount)
    
    # Calculate the difference between the final price and the maximum amount Martin decided to spend
    price_difference = max_price - final_price
    
    result = price_difference
    return result

print(solution())