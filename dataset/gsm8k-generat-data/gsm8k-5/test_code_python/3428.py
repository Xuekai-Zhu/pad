def solution():
    original_price = 24 * 7  # Jorge spent $7 per ticket
    discount_percent = 50  # Jorge received a 50% discount
    discount_amount = original_price * (discount_percent / 100)  # Calculate the discount amount
    final_price = original_price - discount_amount  # Calculate the final price after the discount

    result = final_price
    return result

print(solution())