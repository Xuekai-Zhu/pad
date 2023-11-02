def solution():
    original_price = 50  # The original price of the dress was $50
    discount_percent = 30  # The store was offering 30% discount on everything

    # Calculate the amount of discount
    discount_amount = original_price * (discount_percent/100)

    # Calculate the final price after discount
    final_price = original_price - discount_amount
    result = final_price
    return result

print(solution())