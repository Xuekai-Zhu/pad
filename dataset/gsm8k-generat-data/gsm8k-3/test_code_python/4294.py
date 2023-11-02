def solution():
    """Sarah starts saving $5.00 a week for 4 weeks.  Then she saves $10.00 a week for the next 4 weeks.  Then she saves $20.00 a week for the next 4 weeks.  How much money has she saved over 12 weeks?"""
    # Calculate the total savings for each period
    savings1 = 5 * 4
    savings2 = 10 * 4
    savings3 = 20 * 4

    # Calculate the total savings over 12 weeks
    total_savings = savings1 + savings2 + savings3

    # Display the total savings
    result = total_savings
    return result

print(solution())