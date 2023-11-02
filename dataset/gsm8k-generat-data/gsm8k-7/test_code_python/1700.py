def solution():
    car_price = 35000
    loan_amount = 20000
    loan_rate = 0.15  # 15% loan rate

    # Calculate the amount of interest on the loan
    loan_interest = loan_amount * loan_rate

    # Calculate the total amount that Mike will need to pay for the car
    total_cost = car_price + loan_interest
    result = total_cost
    return result

print(solution())