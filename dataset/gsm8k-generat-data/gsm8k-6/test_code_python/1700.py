def solution():
    # Calculate the total cost of the car, including the loan from the bank
    loan_amount = 20000  # amount of loan from the bank
    loan_rate = 0.15  # loan interest rate
    loan_interest = loan_amount * loan_rate  # total interest on the loan
    car_cost = 35000  # cost of the car
    total_cost = car_cost + loan_amount + loan_interest  # total cost of the car including the loan
    result = total_cost
    return result

print(solution())