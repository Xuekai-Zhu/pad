def solution():
    """Bernie loves eating chocolate. He buys two chocolates every week at the local store. One chocolate costs him $3. In a different store, there is a long-term promotion, during which each chocolate costs only $2. How much would Bernie save in three weeks, if he would buy his chocolates in this store instead of his local one?"""
    local_price = 3
    promo_price = 2
    weekly_chocolates = 2
    weeks = 3
    local_total = weekly_chocolates * weeks * local_price
    promo_total = weekly_chocolates * weeks * promo_price
    savings = local_total - promo_total
    result = savings
    return result

print(solution())