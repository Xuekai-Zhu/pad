def solution():
    
    total_debt = 50
    first_payment = 12
    second_payment = first_payment + 3
    paid_off = first_payment + second_payment
    remaining_debt = total_debt - paid_off
    result = remaining_debt
    return result

print(solution())