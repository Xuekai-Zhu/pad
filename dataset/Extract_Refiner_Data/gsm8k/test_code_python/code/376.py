def solution():
    
    # Define the initial loan and interest rate
    loan = 3665
    interest_rate = 0.1

    # Calculate the interest earned over 5 months
    interest = loan * interest_rate * 5

    # Calculate the total amount Karan has to pay over 5 months
    total_pay = loan + interest

    # Calculate the amount Karan needs to pay per month
    monthly_payment = total_pay / 5

    # Display the amount Karan needs to pay per month
    result = monthly_payment
    return result

print(solution())