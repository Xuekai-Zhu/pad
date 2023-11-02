def solution():
    
    current_balance = 4000
    first_client_payment = current_balance / 2
    second_client_payment = 2/5 * first_client_payment + first_client_payment
    combined_payment = first_client_payment + second_client_payment
    third_client_payment = combined_payment * 2
    total_payment = first_client_payment + second_client_payment + third_client_payment
    result = current_balance + total_payment
    return result

print(solution())