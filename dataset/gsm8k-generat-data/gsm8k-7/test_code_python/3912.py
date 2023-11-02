def solution():
    down_payment = 5000.0
    monthly_payment = 250.0
    loan_term = 5  # years

    # Calculate the total amount Quincy will pay over the course of the loan
    total_paid = monthly_payment * 12 * loan_term

    # Subtract the down payment to get the price of the car
    car_price = total_paid + down_payment
    result = car_price
    return result

print(solution())