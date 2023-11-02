def solution():
    # Calculate the total cost of the peaches before any discount
    total_cost_before_discount = 400 * 0.40

    # Calculate the number of $10 purchases Kataleya made
    num_purchases = total_cost_before_discount // 10

    # Calculate the total discount that Kataleya gets
    total_discount = num_purchases * 2

    # Calculate the total cost of the peaches after discount
    total_cost_after_discount = total_cost_before_discount - total_discount

    result = total_cost_after_discount
    return result

print(solution())