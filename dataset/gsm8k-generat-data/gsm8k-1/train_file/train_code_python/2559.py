def solution():
    """Mr. Smith has incurred a 2% finance charge because he was not able to pay on time for his balance worth $150. If he plans to settle his balance today, how much will Mr. Smith pay?"""
    balance = 150
    finance_charge = balance * 0.02
    total_payment = balance + finance_charge
    result = total_payment
    return result

print(solution())