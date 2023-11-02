def solution():
    sweater_cost = 20
    fraction_spent_on_makeup = 3/4
    fraction_left = 1 - fraction_spent_on_makeup

    # Calculate the amount of money Leila spent on make-up
    makeup_cost = fraction_spent_on_makeup * (sweater_cost / fraction_left)

    # Calculate the original savings
    original_savings = makeup_cost + sweater_cost
    result = original_savings
    return result

print(solution())