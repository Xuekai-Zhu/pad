def solution():
    """It took Alice three months to save up to buy new shoes. If she saved 10 dollars the first month and 30 more each month, how much did she have saved by the end of the third month?"""
    # Alice's initial savings
    savings = 10

    # Amount saved in the second month
    savings += 30

    # Amount saved in the third month
    savings += 30 * 2

    # Total savings after three months
    total_savings = savings

    # Display Alice's total savings
    result = total_savings
    return result

print(solution())