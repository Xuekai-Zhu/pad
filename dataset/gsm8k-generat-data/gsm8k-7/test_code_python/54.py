def solution():
    total_earnings = 28.0
    milkshake_cost = total_earnings / 7.0
    
    # Calculate the amount of money Leah has left after buying a milkshake
    money_left = total_earnings - milkshake_cost
    
    # Calculate the amount of money Leah puts in her savings account
    savings_amount = money_left / 2.0
    
    # Calculate the amount of money Leah has left in her wallet
    wallet_amount = money_left - savings_amount
    
    # Calculate the amount of money Leah lost when her dog shredded her wallet
    amount_lost = money_left - 1.0
    
    result = amount_lost
    return result

print(solution())