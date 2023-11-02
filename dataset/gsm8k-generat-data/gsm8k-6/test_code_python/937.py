def solution():
    original_price = 50  # price of the dress before discount
    discount_percentage = 30  # percentage discount offered by the store
    discount_amount = (discount_percentage/100) * original_price  # calculate the amount of discount
    final_price = original_price - discount_amount  # calculate the final price
    result = final_price
    return result

print(solution())