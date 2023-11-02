def solution():
    chocolates_per_week = 2
    local_store_price = 3
    promo_store_price = 2
    num_weeks = 3

    # Calculate the total cost of buying chocolates from the local store for three weeks
    local_store_cost = chocolates_per_week * local_store_price * num_weeks

    # Calculate the total cost of buying chocolates from the promo store for three weeks
    promo_store_cost = chocolates_per_week * promo_store_price * num_weeks

    # Calculate the amount Bernie would save by buying from the promo store
    savings = local_store_cost - promo_store_cost
    result = savings
    return result

print(solution())