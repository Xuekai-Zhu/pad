def solution():
    house_cost = 480000
    trailer_cost = 120000
    num_years = 20
    num_months = num_years * 12

    # Calculate the monthly payment for the house
    house_monthly_payment = house_cost / (num_months * 1.0)

    # Calculate the monthly payment for the trailer
    trailer_monthly_payment = trailer_cost / (num_months * 1.0)

    # Calculate the difference in monthly payments
    monthly_payment_diff = house_monthly_payment - trailer_monthly_payment
    result = monthly_payment_diff
    return result

print(solution())