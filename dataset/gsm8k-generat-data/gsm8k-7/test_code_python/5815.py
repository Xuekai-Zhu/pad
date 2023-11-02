def solution():
    price_with_discount = 7500
    discount_percentage = 0.25 # 25% less than original price

    # Calculate the original price of the car
    original_price = price_with_discount / (1 - discount_percentage)
    result = original_price
    return result

print(solution())