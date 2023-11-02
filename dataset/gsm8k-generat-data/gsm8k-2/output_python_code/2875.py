def solution():
    """Aaron wants to purchase a guitar under a payment plan of $100.00 per month for 12 months. His father has agreed to lend him the entire amount for the guitar, plus a one-time 10% interest fee for the entire loan. With interest, how much money will Aaron owe his dad?"""
    loan_amount = 100 * 12
    interest_rate = 0.1
    interest_fee = loan_amount * interest_rate
    total_amount = loan_amount + interest_fee
    result = total_amount
    return result

print(solution())