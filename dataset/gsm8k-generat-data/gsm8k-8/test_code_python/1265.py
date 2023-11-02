def solution():
    # Calculate the total cost of the bills for the first 4 months
    first_four_months_cost = 30 * 4

    # Calculate the total cost of the bills for the last 2 months
    last_two_months_cost = 24 * 2

    # Calculate the total cost of the bills for all 6 months
    total_cost = first_four_months_cost + last_two_months_cost

    # Calculate the average monthly bill for all 6 months
    average_monthly_bill = total_cost / 6
    result = average_monthly_bill
    return result

print(solution())