def solution():
    # Calculate cost of two chocolates for three weeks in local store
    local_cost = 3 * 2 * 3

    # Calculate cost of two chocolates for three weeks in promotion store
    promotion_cost = 2 * 2 * 3

    # Calculate the amount saved by buying from promotion store
    saved_amount = local_cost - promotion_cost

    result = saved_amount
    return result

print(solution())