def solution():
    """John buys a vacuum cleaner for $250 and a dishwasher for $450.  She has a $75 off coupon.  How much did he spend?"""
    # Define the prices of the vacuum cleaner and dishwasher
    VACUUM_PRICE = 250
    DISHWASHER_PRICE = 450

    # Define the value of John's coupon
    COUPON_VALUE = 75

    # Calculate the total cost before the coupon
    total_cost_before_coupon = VACUUM_PRICE + DISHWASHER_PRICE

    # Calculate the total cost after the coupon
    total_cost_after_coupon = total_cost_before_coupon - COUPON_VALUE

    # Display the total cost after the coupon
    result = total_cost_after_coupon
    return result

print(solution())