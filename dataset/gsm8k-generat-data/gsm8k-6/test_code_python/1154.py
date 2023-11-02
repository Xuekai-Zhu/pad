def solution():
    # Calculate the cost of the stockings before the discount
    cost_before_discount = 5 * 9 * 20  # Pearl has 5 grandchildren and 4 children to order stockings for

    # Calculate the discount
    discount = 0.1 * cost_before_discount

    # Calculate the total cost with the discount
    cost_with_discount = cost_before_discount - discount

    # Calculate the total cost with monogramming
    total_cost = cost_with_discount + 5 * 9 * 5  # monogramming costs $5.00 per stocking

    result = total_cost
    return result

print(solution())