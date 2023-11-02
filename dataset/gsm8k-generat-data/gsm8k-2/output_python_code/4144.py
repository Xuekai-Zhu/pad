def solution():
    """Ben spends 20% of his after-tax income on his car. If his car payment is $400 and he pays 1/3 of his gross income in taxes, how much does he make per month before taxes?"""
    car_payment = 400
    car_percentage = 0.2
    tax_percentage = 1/3
    net_income = car_payment / car_percentage
    gross_income = net_income / (1 - tax_percentage)
    result = gross_income
    return result

print(solution())