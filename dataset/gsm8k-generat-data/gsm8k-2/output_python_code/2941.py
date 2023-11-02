def solution():
    """Gunther just financed a John Deere tractor through the dealership. If his monthly payment is $150.00 a month, for 5 years, with no interest, how much did he finance the tractor for?"""
    monthly_payment = 150
    years = 5
    total_payments = years * 12
    total_cost = total_payments * monthly_payment
    result = total_cost
    return result

print(solution())