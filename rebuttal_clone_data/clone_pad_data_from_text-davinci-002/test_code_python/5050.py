def solution():
    total_cost = 450
    down_payment = 100
    monthly_payment_1 = 40
    monthly_payment_2 = 35
    monthly_payment_3 = 30
    total_saved = total_cost - down_payment - (monthly_payment_1 * 4) - (monthly_payment_2 * 4) - (monthly_payment_3 * 4)
    result = total_saved
    return result

print(solution())