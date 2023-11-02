def solution():
    # Calculate the total amount saved by Kathleen
    total_savings = 21 + 46 + 45  # savings in June, July, and August
    total_spending = 12 + 54  # spending on school supplies and clothes
    remaining_balance = total_savings - total_spending  # remaining balance
    aunt_bonus = 0  # initialize Aunt's bonus to be zero
    
    if remaining_balance > 125:
        aunt_bonus = 25  # Aunt will give $25 bonus if Kathleen saves more than $125
    
    final_balance = remaining_balance + aunt_bonus  # final balance including Aunt's bonus
    
    result = final_balance
    return result

print(solution())