def solution():
    """Janeth borrowed $2000 and promised to return it with an additional 10% of the amount. If she is going to pay $165 a month for 12 months, how much will be Janeth's remaining balance by then?"""
    borrowed_amount = 2000
    interest_rate = 0.1
    monthly_payment = 165
    months = 12
    
    total_amount_to_pay = borrowed_amount + (borrowed_amount * interest_rate)
    remaining_balance = total_amount_to_pay - (monthly_payment * months)
    
    result = remaining_balance
    return result

print(solution())