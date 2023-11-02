def solution():
    """Ben spends 20% of his after-tax income on his car. If his car payment is $400 and he pays 1/3 of his gross income in taxes, how much does he make per month before taxes?"""
    # Define the car payment and the tax rate
    car_payment = 400
    tax_rate = 1/3

    # Calculate the after-tax income
    after_tax_income = car_payment / 0.2
    
    # Calculate the before-tax income
    before_tax_income = after_tax_income / (1 - tax_rate)

    # Return the result
    result = before_tax_income
    return result

print(solution())