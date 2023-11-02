def solution():
    # Calculate the cost of the jeans after the summer discount
    summer_discount = 0.5
    jeans_cost_after_discount = 14.5 * (1 - summer_discount)

    # Calculate the cost of the jeans after the summer discount and Wednesday discount
    wednesday_discount = 10
    jeans_cost_after_wednesday_discount = jeans_cost_after_discount - wednesday_discount

    # Calculate the original cost of the jeans before all discounts
    original_jeans_cost = jeans_cost_after_wednesday_discount / (1 - summer_discount)
    result = original_jeans_cost
    return result

print(solution())