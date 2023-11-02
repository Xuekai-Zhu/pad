def solution():
    """Daniel buys a magazine costing $0.85 and a pencil costing $0.50. He pays with a coupon that gives him $0.35 off. How much does he spend?"""
    # Define the cost of the magazine and the pencil
    MAGAZINE_COST = 0.85
    PENCIL_COST = 0.50

    # Define the amount of the coupon
    COUPON_AMOUNT = 0.35

    # Calculate the total cost before the coupon
    total_cost_before_coupon = MAGAZINE_COST + PENCIL_COST

    # Calculate the total cost after the coupon
    total_cost_after_coupon = total_cost_before_coupon - COUPON_AMOUNT

    # Display the total cost after the coupon
    result = total_cost_after_coupon
    return result

print(solution())