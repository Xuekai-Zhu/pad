def solution():
    """John buys a vacuum cleaner for $250 and a dishwasher for $450. She has a $75 off coupon. How much did he spend?"""
    # Define the prices of the vacuum cleaner and dishwasher
    vacuum_cleaner_price = 250
    dishwasher_price = 450

    # Define the value of the coupon
    coupon_value = 75

    # Calculate the total cost before the coupon
    total_cost = vacuum_cleaner_price + dishwasher_price

    # Apply the coupon to the total cost
    total_cost -= coupon_value

    # Return the result
    result = total_cost
    return result

print(solution())