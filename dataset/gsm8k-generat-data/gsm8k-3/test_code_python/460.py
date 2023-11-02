def solution():
    """
    John gets a bonus that's the same percentage every year.  Last year he made $100,000 and got a $10,000 bonus.  This year he makes $200,000.  How much will John make this year when adding both his total pay and bonus together?
    """
    # Calculate the percentage increase in John's salary
    percent_increase = (200000 - 100000) / 100000

    # Calculate John's bonus for this year
    bonus = percent_increase * 10000

    # Calculate John's total pay for this year
    total_pay = 200000 + bonus

    # Display John's total pay for this year
    result = total_pay
    return result

print(solution())