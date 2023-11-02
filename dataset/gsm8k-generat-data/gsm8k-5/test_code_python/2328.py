def solution():
    discounted_price = 51  # The shoes were bought for $51
    discount_percentage = 75  # The shoes were marked 75% off

    # Calculate the original price of the shoes
    original_price = discounted_price / (1 - (discount_percentage / 100))
    result = original_price
    return result

print(solution())