def solution():
    first_four_months = 30  # average monthly bill for first 4 months
    last_two_months = 24  # average monthly bill for last 2 months

    # Calculate the total cost for all 6 months
    total_cost = (first_four_months * 4) + (last_two_months * 2)

    # Calculate the average monthly bill for all 6 months
    avg_monthly_bill = total_cost / 6
    result = avg_monthly_bill
    return result

print(solution())