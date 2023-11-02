def solution():
    chocolates_per_week = 2  # Bernie buys two chocolates every week
    local_cost = 3  # One chocolate costs $3 at the local store
    promo_cost = 2  # One chocolate costs $2 during the promotion
    weeks = 3  # Bernie wants to know how much he would save in 3 weeks

    # Calculate the total cost at the local store
    local_total_cost = chocolates_per_week * local_cost * weeks

    # Calculate the total cost during the promotion
    promo_total_cost = chocolates_per_week * promo_cost * weeks

    # Calculate the difference in cost
    savings = local_total_cost - promo_total_cost
    result = savings
    return result

print(solution())