def solution():
    
    current_balance = 4000
    first_payment = current_balance / 2
    second_payment = first_payment * (2/5) + first_payment
    third_payment = (first_payment + second_payment) * 2
    total_payment = first_payment + second_payment + third_payment
    new_balance = current_balance + total_payment
    result = new_balance
    return result

print(solution())