def solution():
    pills_per_day = 2  # John needs to take 2 pills a day
    cost_per_pill = 1.5  # One pill costs $1.5
    days_per_month = 30  # There are 30 days in a month
    insurance_coverage = 0.4  # The insurance covers 40% of the cost

    # Calculate the total cost before insurance coverage
    total_cost = pills_per_day * cost_per_pill * days_per_month

    # Calculate the amount covered by insurance
    insurance_amount = total_cost * insurance_coverage

    # Calculate the out-of-pocket cost for John
    out_of_pocket_cost = total_cost - insurance_amount
    result = out_of_pocket_cost
    return result

print(solution())