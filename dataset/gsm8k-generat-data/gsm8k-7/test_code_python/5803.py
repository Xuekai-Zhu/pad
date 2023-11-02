def solution():
    magazine_cost = 0.85
    pencil_cost = 0.50
    coupon_discount = 0.35

    # Calculate the total cost before coupon
    total_cost = magazine_cost + pencil_cost

    # Apply the coupon discount
    total_cost -= coupon_discount

    result = total_cost
    return result

print(solution())