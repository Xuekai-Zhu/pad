def solution():
    apple_price = 5  # Apples cost $5 per kilogram
    discount_rate = 0.4  # Hannah gets a 40% discount on each kilogram of apples she buys
    apple_weight = 10  # Hannah wants to buy 10 kilograms of apples

    # Calculate the price of the apples before the discount
    original_price = apple_price * apple_weight

    # Calculate the discount amount
    discount_amount = original_price * discount_rate

    # Calculate the final price of the apples after the discount
    final_price = original_price - discount_amount
    result = final_price
    return result

print(solution())