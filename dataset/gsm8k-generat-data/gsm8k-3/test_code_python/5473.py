def solution():
    """
    Jill likes to do small jobs online.  She makes $10 a day for her first month working online, and double that per day in her second month.  Her third month she makes the same amount per day as the previous month, but only works every other day.  How much did she make over three months, assuming each month is 30 days long?
    """
    # Define the amount Jill makes per day in each month
    month1_pay = 10
    month2_pay = 20
    month3_pay = 40

    # Define the number of days Jill works in each month
    month1_days = 30
    month2_days = 30
    month3_days = 15

    # Calculate Jill's earnings in each month
    month1_earnings = month1_days * month1_pay
    month2_earnings = month2_days * month2_pay
    month3_earnings = month3_days * month3_pay

    # Calculate Jill's total earnings over the three months
    total_earnings = month1_earnings + month2_earnings + month3_earnings

    # Display Jill's total earnings
    result = total_earnings
    return result

print(solution())