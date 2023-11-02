def solution():
    """John decides to get a loan by mortgaging his home. His house is worth $250,000. He gets a loan worth 40% of that. He uses 60% of that to pay off his debts. How much money did he have leftover after paying debt?"""
    house_value = 250000
    loan_percent = 0.4
    loan_amount = house_value * loan_percent
    debt_payment_percent = 0.6
    debt_payment = loan_amount * debt_payment_percent
    leftover_money = loan_amount - debt_payment
    result = leftover_money
    return result

print(solution())