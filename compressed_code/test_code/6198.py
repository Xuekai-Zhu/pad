def solution():
    
    num_students = 25
    full_payment = 50
    half_payment = full_payment / 2
    num_full_payments = num_students - 4
    total_paid = (num_full_payments * full_payment) + (4 * half_payment)
    result = total_paid
    return result

print(solution())