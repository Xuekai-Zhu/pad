def solution():
    # Calculate the discounted price for 5 chairs
    discount_price = 20 * 0.75  # 25% discount

    # Calculate the discounted price for the remaining 3 chairs
    extra_discount_price = (20 * 0.75) * (1/3)  # 1/3 off the discounted price

    # Calculate the total price for all 8 chairs
    total_price = (discount_price * 5) + (extra_discount_price * 3)
    result = total_price
    return result

print(solution())