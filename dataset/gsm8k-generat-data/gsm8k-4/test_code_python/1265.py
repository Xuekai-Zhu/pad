def solution():
    """A family's water and electricity bills average $30 a month for the first 4 months and $24 a month for the last 2 months. If the family's bills were averaged over all 6 months, what would the average monthly bill be?"""
    # Define the bills for the first 4 months
    first_bills = 30 * 4

    # Define the bills for the last 2 months
    last_bills = 24 * 2

    # Calculate the total bills for all 6 months
    total_bills = first_bills + last_bills

    # Calculate the average monthly bill for all 6 months
    average_bill = total_bills / 6

    result = average_bill
    return result

print(solution())