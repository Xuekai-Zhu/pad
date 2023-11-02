def solution():
    """A family's water and electricity bills average $30 a month for the first 4 months and $24 a month for the last 2 months. If the family's bills were averaged over all 6 months, what would the average monthly bill be?"""
    # Define the total cost for the first 4 months and the last 2 months
    first_4_total = 30 * 4
    last_2_total = 24 * 2

    # Calculate the total cost for all 6 months
    total_cost = first_4_total + last_2_total

    # Calculate the average monthly bill for all 6 months
    average_monthly_bill = total_cost / 6

    # Display the average monthly bill
    result = average_monthly_bill
    return result

print(solution())