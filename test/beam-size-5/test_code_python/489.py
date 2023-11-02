def solution():
    num_packs = 2
    pack_price = 4.0
    discount = 0.0
    coupon_amount = 2.0

    # Calculate the total cost of buying 2 packs of razors
    total_cost = num_packs * pack_price

    # Calculate the total cost of buying 2 packs of razors with the coupon
    total_cost -= coupon_amount

    # Calculate the cost per individual razor
    cost_per_rabor = total_cost / num_packs
    result = cost_per_rabor
    return result

print(solution())