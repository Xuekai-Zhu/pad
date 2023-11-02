def solution():
    slippers_price = 50.00  # Original price of the slippers
    discount_percent = 10  # 10% Discount on the slippers
    embroidery_cost_per_shoe = 5.50  # Cost of embroidery per shoe
    shipping_cost = 10.00  # Flat rate shipping cost

    # Calculate the discounted price of the slippers
    discounted_price = slippers_price - ((discount_percent/100.0)*slippers_price)

    # Calculate the total cost of embroidery
    embroidery_cost = embroidery_cost_per_shoe * 2  # Multiply cost per shoe by 2 slippers

    # Calculate the total cost of the order
    total_cost = discounted_price + embroidery_cost + shipping_cost
    result = total_cost
    return result

print(solution())