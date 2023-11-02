def solution():
    vacuum_cleaner_cost = 250  # John buys a vacuum cleaner for $250
    dishwasher_cost = 450  # John buys a dishwasher for $450
    coupon_amount = 75  # John has a coupon worth $75

    # Calculate the total cost before applying the coupon
    total_cost_before_coupon = vacuum_cleaner_cost + dishwasher_cost

    # Calculate the total cost after applying the coupon
    total_cost_after_coupon = total_cost_before_coupon - coupon_amount
    result = total_cost_after_coupon
    return result

print(solution())