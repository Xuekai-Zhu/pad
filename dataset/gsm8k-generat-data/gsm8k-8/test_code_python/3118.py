def solution():
    # Define the cost of the car and the down payment
    car_cost = 32000
    down_payment = 8000

    # Calculate the total amount Jason needs to finance
    total_financed = car_cost - down_payment

    # Calculate the monthly payment before interest
    monthly_payment = total_financed / 48

    # Calculate the monthly interest amount
    monthly_interest = 0.05 * monthly_payment

    # Calculate the total monthly payment
    total_monthly_payment = monthly_payment + monthly_interest

    result = total_monthly_payment
    return result

print(solution())