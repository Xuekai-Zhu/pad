def solution():
    house_cost = 480000
    trailer_cost = 120000
    loan_years = 20
    loan_months = loan_years * 12

    # Calculate the monthly payment for the house loan
    house_interest_rate = 0.04
    house_monthly_rate = house_interest_rate / 12
    house_monthly_payment = house_cost * (house_monthly_rate / (1 - ((1 + house_monthly_rate) ** (-loan_months))))

    # Calculate the monthly payment for the trailer loan
    trailer_interest_rate = 0.08
    trailer_monthly_rate = trailer_interest_rate / 12
    trailer_monthly_payment = trailer_cost * (trailer_monthly_rate / (1 - ((1 + trailer_monthly_rate) ** (-loan_months))))

    # Calculate the difference between the monthly payments
    monthly_payment_difference = house_monthly_payment - trailer_monthly_payment
    result = monthly_payment_difference
    return result

print(solution())