def solution():
    """Sarah starts saving $5.00 a week for 4 weeks. Then she saves $10.00 a week for the next 4 weeks. Then she saves $20.00 a week for the next 4 weeks. How much money has she saved over 12 weeks?"""
    # Define the saving amounts for each period
    period1_savings = 5 * 4
    period2_savings = 10 * 4
    period3_savings = 20 * 4

    # Calculate the total savings over 12 weeks
    total_savings = period1_savings + period2_savings + period3_savings

    # return the result
    result = total_savings
    return result

print(solution())