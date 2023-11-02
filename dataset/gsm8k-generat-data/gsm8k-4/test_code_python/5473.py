def solution():
    """Jill likes to do small jobs online. She makes $10 a day for her first month working online, and double that per day in her second month. Her third month she makes the same amount per day as the previous month, but only works every other day. How much did she make over three months, assuming each month is 30 days long?"""
    # Define the number of days in each month
    DAYS_IN_MONTH = 30

    # Define the daily earnings in each month
    month1_earnings = 10
    month2_earnings = month1_earnings * 2
    month3_earnings = month2_earnings

    # Calculate the total earnings in each month
    month1_total = month1_earnings * DAYS_IN_MONTH
    month2_total = month2_earnings * DAYS_IN_MONTH
    month3_total = month3_earnings * (DAYS_IN_MONTH // 2)

    # Calculate the overall total earnings
    total_earnings = month1_total + month2_total + month3_total

    # Return the result
    result = total_earnings
    return result

print(solution())