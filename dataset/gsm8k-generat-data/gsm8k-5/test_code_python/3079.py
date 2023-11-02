def solution():
    original_cost = 14.50  # Before any discounts are applied, a pair of jeans costs $14.50
    summer_discount = 0.5  # There is a 50% discount for all items during the summer
    wednesday_discount = 10.00  # On Wednesdays, there is an additional $10.00 off on all jeans

    # Calculate the cost of the jeans after the summer discount is applied
    cost_after_summer_discount = original_cost * (1 - summer_discount)

    # Calculate the cost of the jeans after the Wednesday discount is applied
    cost_after_wednesday_discount = cost_after_summer_discount - wednesday_discount

    # Calculate the original cost of the jeans before any discounts were applied
    original_cost_before_discounts = cost_after_wednesday_discount / (1 - summer_discount)
    result = original_cost_before_discounts
    return result

print(solution())