def solution():
    original_price = 90  # The original price of the boots is $90
    discount_percent = 20  # There is a discount of 20%

    # Calculate the discounted price of the boots
    discounted_price = original_price * (100 - discount_percent) / 100

    result = discounted_price
    return result

print(solution())