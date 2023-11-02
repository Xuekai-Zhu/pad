def solution():
    """Bernie loves eating chocolate. He buys two chocolates every week at the local store. One chocolate costs him $3. In a different store, there is a long-term promotion, during which each chocolate costs only $2. How much would Bernie save in three weeks, if he would buy his chocolates in this store instead of his local one?"""
    # Calculate the cost of two chocolates in the local store per week
    local_cost = 3 * 2      # Two chocolates at $3 each

    # Calculate the cost of two chocolates in the other store per week
    promo_cost = 2 * 2      # Two chocolates at $2 each

    # Calculate the savings per week
    savings_per_week = local_cost - promo_cost

    # Calculate the total savings in three weeks
    total_savings = savings_per_week * 3

    # Display the total savings
    result = total_savings
    return result

print(solution())