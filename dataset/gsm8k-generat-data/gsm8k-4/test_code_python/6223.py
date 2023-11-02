def solution():
    """Bernie loves eating chocolate. He buys two chocolates every week at the local store. One chocolate costs him $3.
    In a different store, there is a long-term promotion, during which each chocolate costs only $2.
    How much would Bernie save in three weeks, if he would buy his chocolates in this store instead of his local one?"""
    
    # Define the number of chocolates Bernie buys each week and their cost
    chocolates_per_week = 2
    local_cost_per_chocolate = 3
    promotion_cost_per_chocolate = 2

    # Calculate the cost of chocolates for three weeks at the local store
    local_cost_three_weeks = chocolates_per_week * local_cost_per_chocolate * 3

    # Calculate the cost of chocolates for three weeks with the promotion
    promotion_cost_three_weeks = chocolates_per_week * promotion_cost_per_chocolate * 3

    # Calculate how much Bernie would save
    savings = local_cost_three_weeks - promotion_cost_three_weeks

    result = savings
    return result

print(solution())