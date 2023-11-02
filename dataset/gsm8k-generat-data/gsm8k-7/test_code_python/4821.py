def solution():
    monthly_cost = 12
    down_payment = 50
    years = 3

    # Calculate the total number of months in 3 years
    total_months = years * 12

    # Calculate the total cost of the monthly payments
    monthly_payment_cost = monthly_cost * total_months

    # Add the down payment to the total cost
    total_cost = monthly_payment_cost + down_payment
    result = total_cost
    return result

print(solution())