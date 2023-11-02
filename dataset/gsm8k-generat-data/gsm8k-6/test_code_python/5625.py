def solution():
    # Calculate the original price Hannah would pay for 10 kg of apples
    original_price = 5 * 10  # $5 per kilogram and she is buying 10 kilograms

    # Calculate the discount she would get
    discount = 0.4 * original_price

    # Calculate the final price after the discount
    final_price = original_price - discount
    result = final_price
    return result

print(solution())