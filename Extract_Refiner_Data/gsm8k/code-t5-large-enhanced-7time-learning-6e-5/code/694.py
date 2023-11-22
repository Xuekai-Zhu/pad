def solution():
    
    # Define the initial paycheck amount
    paycheck = 2400

    # Calculate the amount Greta puts into her retirement account
    retirement_amount = paycheck * 0.5

    # Calculate the amount Greta spends on her car payment
    car_payment = paycheck * 0.2

    # Calculate the total amount Greta has left to spend
    total_spent = retirement_amount + car_payment

    # Display the total amount Greta has left to spend
    result = total_spent
    return result

print(solution())