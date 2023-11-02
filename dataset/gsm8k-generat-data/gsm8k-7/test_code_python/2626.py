def solution():
    original_price = 50.00
    discount = 0.10  # 10% discount
    embroidery_price = 5.50
    shipping_price = 10.00

    # Calculate the discounted price of the slippers
    discounted_price = original_price * (1 - discount)

    # Calculate the total cost of the slippers with embroidery and shipping
    total_cost = discounted_price + (embroidery_price * 2) + shipping_price
    result = total_cost
    return result

print(solution())