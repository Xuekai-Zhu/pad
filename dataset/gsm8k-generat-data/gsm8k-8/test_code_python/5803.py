def solution():
    # Define the prices of the magazine and pencil
    magazine_price = 0.85
    pencil_price = 0.5

    # Calculate the total cost before the coupon
    total_cost_before_coupon = magazine_price + pencil_price

    # Apply the coupon
    total_cost_after_coupon = total_cost_before_coupon - 0.35

    result = total_cost_after_coupon
    return result

print(solution())