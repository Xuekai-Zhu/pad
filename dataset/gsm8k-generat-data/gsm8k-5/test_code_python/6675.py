def solution():
    original_price = 20  # Each t-shirt originally costs $20
    discount = 0.5  # The t-shirts are 50% off
    quantity = 6  # James buys 6 t-shirts

    # Calculate the total cost before the discount
    total_original_cost = original_price * quantity

    # Calculate the total discounted cost
    total_discounted_cost = total_original_cost * (1 - discount)

    result = total_discounted_cost
    return result

print(solution())