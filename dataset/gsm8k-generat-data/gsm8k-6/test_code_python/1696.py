def solution():
    # Calculate Silas' payment
    silas_payment = 150/2 

    # Calculate the remaining payment after Silas' payment
    remaining_payment = 150/2 

    # Calculate the payment for each of the remaining friends, including the tip
    payment_per_friend = remaining_payment/5 * 1.1 

    result = payment_per_friend
    return result

print(solution())