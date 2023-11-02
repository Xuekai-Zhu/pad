def solution():
    """Aaron wants to purchase a guitar under a payment plan of $100.00 per month for 12 months. His father has agreed to lend him the entire amount for the guitar, plus a one-time 10% interest fee for the entire loan. With interest, how much money will Aaron owe his dad?"""
    monthly_payment = 100
    loan_duration = 12
    loan_amount = monthly_payment * loan_duration
    interest_rate = 0.1
    interest_fee = loan_amount * interest_rate
    total_owed = loan_amount + interest_fee
    result = total_owed
    return result

print(solution())