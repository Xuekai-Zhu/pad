def solution():
    # Calculate Wilson's balance two months ago
    balance_two_months_ago = 150
    
    # Calculate Wilson's balance last month
    balance_last_month = balance_two_months_ago + 17
    
    # Calculate Wilson's balance after withdrawal
    balance_after_withdrawal = balance_last_month - withdrawal
    
    # Calculate Wilson's current balance
    current_balance = balance_after_withdrawal + 21
    
    # Calculate the amount Wilson withdrew last month
    withdrawal = current_balance - 16 - balance_two_months_ago
    
    result = withdrawal
    return result

print(solution())