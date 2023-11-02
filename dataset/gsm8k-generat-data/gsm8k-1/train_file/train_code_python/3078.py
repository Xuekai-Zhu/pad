def solution():
    """For the summer, the clothing store has a 50% discount for all items. On Wednesdays, there is an additional $10.00 off on all jeans after the summer discount is applied. Before the sales tax applies, the cost of a pair of jeans is $14.50. How much was the original cost for the jeans before all the discounts?"""
    original_cost = 29
    wednesday_discount = 10
    discounted_cost = original_cost / 2
    final_cost = discounted_cost - wednesday_discount
    result = final_cost
    return result

print(solution())