def solution():
    couch_cost = 2500
    sectional_cost = 3500
    other_cost = 2000
    discount_rate = 0.1

    # Calculate the total cost of everything without discount
    total_cost_without_discount = couch_cost + sectional_cost + other_cost

    # Calculate the amount of discount
    discount_amount = total_cost_without_discount * discount_rate

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_without_discount - discount_amount

    result = total_cost_after_discount
    return result

print(solution())