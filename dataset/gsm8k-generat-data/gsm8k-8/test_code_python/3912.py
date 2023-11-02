def solution():
    # Calculate the total number of months in 5 years
    total_months = 5 * 12

    # Subtract the number of months with the down payment from the total months
    loan_months = total_months - 1 

    # Calculate the total loan amount by multiplying the monthly payment by the number of loan months
    total_loan_amount = loan_months * 250

    # Add the down payment to the total loan amount to get the price of the car
    car_price = total_loan_amount + 5000
    result = car_price
    return result

print(solution())