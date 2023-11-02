def solution():
    full_price = 85
    discount_1 = 0.20
    discount_2 = 0.25

    # Calculate the discounted price for officers with at least 1 year of service
    discount_1_price = full_price * (1 - discount_1)

    # Calculate the discounted price for officers with at least 3 years of service
    discount_2_price = discount_1_price * (1 - discount_2)

    result = discount_2_price
    return result

print(solution())