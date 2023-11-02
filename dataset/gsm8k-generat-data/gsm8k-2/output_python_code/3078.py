def solution():
    """For the summer, the clothing store has a 50% discount for all items. On Wednesdays, there is an additional $10.00 off on all jeans after the summer discount is applied. Before the sale tax applies, the cost of a pair of jeans is $14.50. How much was the original cost for the jeans before all the discounts?"""
    jeans_cost = 14.5
    summer_discount = 0.5
    wednesday_discount = 10.0
    cost_after_summer_discount = jeans_cost * (1 - summer_discount)
    cost_after_wednesday_discount = cost_after_summer_discount - wednesday_discount
    original_cost = cost_after_wednesday_discount / (1 - summer_discount)
    result = original_cost
    return result

print(solution())