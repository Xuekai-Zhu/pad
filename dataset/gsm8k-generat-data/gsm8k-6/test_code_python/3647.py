def solution():
    # Calculate the total cost of the order after the first discount
    cost_before_senior_discount = 7.5 - 2.5  # cost of order after $2.50 coupon is applied
    cost_after_senior_discount = cost_before_senior_discount * 0.8  # cost of order after 20% senior citizen discount
    result = round(cost_after_senior_discount, 2)  # round to two decimal places for currency
    return result

print(solution())