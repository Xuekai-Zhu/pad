def solution():
    
    # Define the prices of the pots and garden soil
    pot_price = 19
    soil_price = 26

    # Calculate the total cost before the coupon
    total_cost_before_coupon = pot_price + soil_price

    # Calculate the total cost after the coupon
    total_cost_after_coupon = total_cost_before_coupon - 7

    # return the result
    result = total_cost_after_coupon
    return result

print(solution())