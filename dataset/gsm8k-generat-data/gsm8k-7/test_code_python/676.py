def solution():
    pills_per_day = 2
    cost_per_pill = 1.5
    insurance_coverage = 0.4  # 40% coverage
    num_days = 30

    # Calculate the total number of pills needed for the month
    num_pills = pills_per_day * num_days

    # Calculate the total cost of all pills before insurance coverage
    total_cost_without_coverage = num_pills * cost_per_pill

    # Calculate the amount covered by insurance
    insurance_amount = total_cost_without_coverage * insurance_coverage

    # Calculate the amount John needs to pay
    amount_to_pay = total_cost_without_coverage - insurance_amount
    result = amount_to_pay
    return result

print(solution())