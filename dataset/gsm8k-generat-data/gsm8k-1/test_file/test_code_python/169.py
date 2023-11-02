def solution():
    """Jessica is trying to figure out how much to pay on all her debts each month. Her student loans have a minimum payment of $300/month, her credit card's minimum is $200/month, and her mortgage's minimum is $500/month. If Jessica wants to pay 50% more than the minimum, how much does she pay in a year?"""
    student_loan_payment = 300 * 1.5
    credit_card_payment = 200 * 1.5
    mortgage_payment = 500 * 1.5
    total_monthly_payment = student_loan_payment + credit_card_payment + mortgage_payment
    total_yearly_payment = total_monthly_payment * 12
    
    return total_yearly_payment

print(solution())