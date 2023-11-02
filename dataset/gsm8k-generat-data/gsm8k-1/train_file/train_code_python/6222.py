def solution():
    """Bernie loves eating chocolate. He buys two chocolates every week at the local store. One chocolate costs him $3. In a different store, there is a long-term promotion, during which each chocolate costs only $2. How much would Bernie save in three weeks, if he would buy his chocolates in this store instead of his local one?"""
    local_store_cost = 3
    other_store_cost = 2
    chocolates_per_week = 2
    weeks = 3
    local_store_total_cost = local_store_cost * chocolates_per_week * weeks
    other_store_total_cost = other_store_cost * chocolates_per_week * weeks
    total_savings = local_store_total_cost - other_store_total_cost
    result = total_savings
    return result

print(solution())