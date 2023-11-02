def solution():
    # Calculate the original price of one shirt
    original_price = 60 / 3  # James buys 3 shirts for $60

    # Calculate the discount amount
    discount_amount = original_price * 0.4  # There is a 40% off sale

    # Calculate the discounted price per shirt
    discounted_price = original_price - discount_amount

    result = discounted_price
    return result

print(solution())