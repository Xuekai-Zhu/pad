def solution():
    """Ben spends 20% of his after-tax income on his car. If his car payment is $400 and he pays 1/3 of his gross income in taxes, how much does he make per month before taxes?"""
    car_payment = 400
    percent_income_on_car = 20
    taxes = 1/3
    after_tax_income = car_payment / (percent_income_on_car / 100)
    before_tax_income = after_tax_income / (1 - taxes)
    result = before_tax_income
    return result

print(solution())