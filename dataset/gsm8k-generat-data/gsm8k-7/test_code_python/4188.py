def solution():
    original_price = 80
    discount_percentage = 0.15  # 15% discount

    # Calculate the amount of discount
    discount_amount = original_price * discount_percentage

    # Calculate the final price after the discount
    final_price = original_price - discount_amount
    result = final_price
    return result

print(solution())