def solution():
    house_price = 480000
    trailer_price = 120000
    years = 20
    months = years * 12
    house_interest_rate = 0.04
    trailer_interest_rate = 0.06

    # Calculate the monthly payment for the house and the trailer
    house_monthly_payment = (house_price * (house_interest_rate/12)) / (1 - ((1 + (house_interest_rate/12)) ** (-months)))
    trailer_monthly_payment = (trailer_price * (trailer_interest_rate/12)) / (1 - ((1 + (trailer_interest_rate/12)) ** (-months)))

    # Calculate the difference in monthly payments
    monthly_payment_difference = house_monthly_payment - trailer_monthly_payment
    result = monthly_payment_difference
    return result

print(solution())