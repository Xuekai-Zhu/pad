def solution():
    car_price = 35000
    loan_amount = 20000
    loan_rate = 0.15

    # Calculate the amount of interest Mike will need to pay on the loan
    loan_interest = loan_amount * loan_rate

    # Calculate the total payment for the car, including the loan and the interest
    total_payment = car_price + loan_amount + loan_interest
    result = total_payment
    return result

print(solution())