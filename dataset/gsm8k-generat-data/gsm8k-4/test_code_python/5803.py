def solution():
    """Daniel buys a magazine costing $0.85 and a pencil costing $0.50. He pays with a coupon that gives him $0.35 off. How much does he spend?"""
    # Define the prices of the magazine and pencil
    magazine_price = 0.85
    pencil_price = 0.50

    # Define the value of the coupon
    coupon_value = 0.35

    # Calculate the total cost before the coupon is applied
    total_cost = magazine_price + pencil_price

    # Apply the coupon to the total cost
    total_cost -= coupon_value

    # Return the final cost
    result = total_cost
    return result

print(solution())