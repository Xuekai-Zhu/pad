def solution():
    vacuum_price = 250
    dishwasher_price = 450
    coupon_amount = 75

    # Calculate the total cost before the coupon
    total_cost = vacuum_price + dishwasher_price

    # Apply the coupon to the total cost
    total_cost -= coupon_amount

    result = total_cost
    return result

print(solution())