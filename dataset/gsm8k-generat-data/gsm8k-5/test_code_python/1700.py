def solution():
    car_price = 35000  # Mike wants to buy a car for $35000
    loan_amount = 20000  # Mike needs to loan $20000
    loan_interest_rate = 0.15  # The loan interest rate is 15%

    # Calculate the total amount Mike needs to pay for the car
    amount_to_pay = car_price + (loan_amount * (1 + loan_interest_rate))
    result = amount_to_pay
    return result

print(solution())