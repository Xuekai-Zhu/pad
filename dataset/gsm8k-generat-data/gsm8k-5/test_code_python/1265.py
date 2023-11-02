def solution():
    first_four_months = 4 * 30  # The average bill for the first 4 months is $30
    last_two_months = 2 * 24  # The average bill for the last 2 months is $24
    total_cost = first_four_months + last_two_months  # The total cost of water and electricity bills for 6 months
    average_monthly_bill = total_cost / 6  # The average monthly bill for 6 months
    result = average_monthly_bill
    return result

print(solution())