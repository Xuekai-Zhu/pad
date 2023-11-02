def solution():
    # Calculate Robert's commission for last month's sales
    commission = 0.1 * 23600  

    # Calculate Robert's total earnings for last month
    total_earnings = 1250 + commission  

    # Calculate the amount Robert saved last month
    savings = 0.2 * total_earnings  

    # Calculate Robert's monthly expenses last month
    expenses = total_earnings - savings  

    result = expenses
    return result

print(solution())