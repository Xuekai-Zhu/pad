def solution():
    # Calculate the original price per shirt
    original_price_per_shirt = 60 / 3

    # Calculate the discount amount
    discount = 0.4

    # Calculate the discounted price per shirt
    discounted_price_per_shirt = original_price_per_shirt - (original_price_per_shirt * discount)

    result = discounted_price_per_shirt
    return result

print(solution())