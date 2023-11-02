def solution():
    # Define the prices of the vacuum cleaner and dishwasher
    vacuum_price = 250
    dishwasher_price = 450

    # Define the value of the coupon
    coupon_value = 75

    # Calculate the total cost before the coupon
    total_cost = vacuum_price + dishwasher_price

    # Apply the coupon
    total_cost -= coupon_value

    result = total_cost
    return result

print(solution())