def solution():
    # Calculate the total cost of Selene's purchase before discount
    total_cost = 2*110 + 3*120  # two instant cameras at $110 and three digital photo frames at $120 each

    # Calculate the discount amount
    discount = 0.05 * total_cost

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount

    result = total_cost_after_discount
    return result

print(solution())