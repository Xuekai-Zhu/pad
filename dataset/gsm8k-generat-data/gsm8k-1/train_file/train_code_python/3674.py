def solution():
    """George wants to borrow $100 from a loan shark. The finance fee starts at 5% and doubles every week. If George plans to borrow for 2 weeks, how much in fees will he have to pay?"""
    loan_amount = 100
    weeks = 2
    finance_fee = 0.05
    total_fees = 0
    
    for i in range(weeks):
        fees_this_week = loan_amount * finance_fee
        total_fees += fees_this_week
        finance_fee *= 2
        
    result = total_fees
    return result

print(solution())