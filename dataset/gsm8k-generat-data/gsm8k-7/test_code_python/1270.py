def solution():
    house_price = 280000
    deposit = 40000
    mortgage_amount = house_price - deposit
    num_years = 10
    num_months = num_years * 12

    # Calculate the monthly payment needed to pay off the mortgage in 10 years
    monthly_payment = mortgage_amount / num_months / 1000  # divide by 1000 to convert to thousands of dollars
    result = monthly_payment
    return result

print(solution())