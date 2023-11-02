def solution():
    """Ben spends 20% of his after-tax income on his car. If his car payment is $400 and he pays 1/3 of his gross income in taxes, how much does he make per month before taxes?"""
    # Define the car payment and the portion of income spent on the car
    car_payment = 400
    car_fraction = 0.20

    # Calculate the after-tax income
    tax_fraction = 1/3
    after_tax_income = car_payment / car_fraction
    gross_income = after_tax_income / (1 - tax_fraction)

    # Display the gross income
    result = gross_income
    return result

print(solution())