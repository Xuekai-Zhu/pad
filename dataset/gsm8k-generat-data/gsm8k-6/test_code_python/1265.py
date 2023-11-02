def solution():
    # Calculate the total bill for the first 4 months
    total_first_months = 30 * 4

    # Calculate the total bill for the last 2 months
    total_last_months = 24 * 2

    # Calculate the total bill for all 6 months
    total_all_months = total_first_months + total_last_months

    # Calculate the average monthly bill for all 6 months
    average_monthly_bill = total_all_months / 6

    result = average_monthly_bill
    return result

print(solution())