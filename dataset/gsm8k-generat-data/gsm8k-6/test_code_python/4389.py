def solution():
    # Calculate the monthly payments for the house and trailer loans
    house_loan = 480000
    trailer_loan = 120000
    interest_rate = 0.05
    years = 20
    months = years * 12
    house_payment = (house_loan * (interest_rate / 12)) / (1 - (1 + (interest_rate / 12)) ** (-months))
    trailer_payment = (trailer_loan * (interest_rate / 12)) / (1 - (1 + (interest_rate / 12)) ** (-months))

    # Calculate the difference in monthly payments
    monthly_difference = house_payment - trailer_payment
    result = round(monthly_difference, 2)
    return result

print(solution())