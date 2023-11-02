def solution():
    # Calculate the cost of the flowers before discount
    pansies_cost = 5 * 2.5  # 5 pansies at $2.50 each
    hydrangea_cost = 12.5  # 1 hydrangea that costs $12.50
    petunias_cost = 5 * 1  # 5 petunias at $1.00 each
    total_cost_before_discount = pansies_cost + hydrangea_cost + petunias_cost

    # Calculate the discount
    discount = 0.1 * total_cost_before_discount

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount

    # Calculate the amount of change Simon will receive
    change = 50 - total_cost_after_discount
    result = change
    return result

print(solution())