def solution():
    # Calculate the discount for Mother's Day
    discount = 0.1  # 10% discount for all mothers

    # Calculate the additional discount for mothers with 3 or more children
    children = 4
    if children >= 3:
        discount += 0.04

    # Calculate the discounted price of the shoes
    shoe_price = 125
    discounted_price = shoe_price * (1 - discount)

    result = discounted_price
    return result

print(solution())