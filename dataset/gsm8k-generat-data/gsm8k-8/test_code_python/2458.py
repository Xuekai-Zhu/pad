def solution():
    # Calculate Robert's commission
    commission = 0.1 * 23600
    
    # Calculate Robert's total earnings
    total_earnings = 1250 + commission
    
    # Calculate the amount allocated to savings
    savings = 0.2 * total_earnings
    
    # Calculate the amount spent on expenses
    expenses = total_earnings - savings
    
    result = expenses
    return result

print(solution())