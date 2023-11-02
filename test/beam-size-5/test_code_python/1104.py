def solution():
    
    # Define the prices of the pots and garden soil
    POTS_PRICE = 19
    SOIL_PRICE = 26

    # Define the coupon amount
    COUPON_AMOUNT = 7

    # Calculate the total cost before the coupon
    total_cost_before_coupon = POTS_PRICE + SOIL_PRICE

    # Calculate the total cost after the coupon
    total_cost_after_coupon = total_cost_before_coupon - COUPON_AMOUNT

    # Display the total cost after the coupon
    result = total_cost_after_coupon
    return result

print(solution())