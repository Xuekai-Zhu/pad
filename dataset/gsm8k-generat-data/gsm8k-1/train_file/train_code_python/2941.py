def solution():
    """Gunther just financed a John Deere tractor through the dealership. If his monthly payment is $150.00 a month, for 5 years, with no interest, how much did he finance the tractor for?"""
    monthly_payment = 150
    loan_duration = 5 # in years
    total_payment = monthly_payment * 12 * loan_duration
    loan_amount = total_payment
    result = loan_amount
    return result

print(solution())