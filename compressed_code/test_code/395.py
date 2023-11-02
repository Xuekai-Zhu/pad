def solution():
    
    total_students = 25
    full_payment = 50
    half_payment = full_payment / 2
    full_pay_students = total_students - 4
    half_pay_students = 4
    total_money_collected = (full_pay_students * full_payment) + (half_pay_students * half_payment)
    result = total_money_collected
    return result

print(solution())