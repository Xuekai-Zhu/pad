def solution():
    inheritance = 20000
    car_price = 18000
    initial_payment = 3000
    num_installments = 6

    # Calculate the remaining price to be paid after the initial payment
    remaining_price = car_price - initial_payment

    # Calculate the total amount to be paid including interest
    total_amount = remaining_price * 1.1

    # Calculate the amount to be paid per installment
    monthly_payment = total_amount / num_installments
    result = monthly_payment
    return result

print(solution())