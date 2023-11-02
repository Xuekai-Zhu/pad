def solution():
    aryan_debt = 1200
    kyro_debt = aryan_debt / 2
    aryan_payment = aryan_debt * 0.6
    kyro_payment = kyro_debt * 0.8
    fernanda_savings = 300
    total_payment = aryan_payment + kyro_payment
    total_savings = fernanda_savings + total_payment
    result = total_savings
    return result

print(solution())