def solution():
    bag_cost = 25.0
    bag_size = 40.0
    serving_size = 1.0
    coupon_amount = 5.0

    # Calculate the cost per ounce before the coupon is applied
    cost_per_ounce = bag_cost / bag_size

    # Calculate the cost per serving before the coupon is applied
    cost_per_serving = cost_per_ounce * serving_size

    # Calculate the new cost of the bag with the coupon applied
    new_bag_cost = bag_cost - coupon_amount

    # Calculate the new cost per ounce after the coupon is applied
    new_cost_per_ounce = new_bag_cost / bag_size

    # Calculate the new cost per serving after the coupon is applied
    new_cost_per_serving = new_cost_per_ounce * serving_size

    # Convert the new cost per serving into cents
    cost_per_serving_in_cents = new_cost_per_serving * 100

    result = cost_per_serving_in_cents
    return result

print(solution())