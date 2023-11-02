def solution():
    car_payment = 400
    percent_income_on_car = 0.2
    tax_percent = 1/3

    # Calculate Ben's after-tax income
    after_tax_income = car_payment / percent_income_on_car

    # Calculate Ben's gross income
    gross_income = after_tax_income / (1 - tax_percent)

    result = gross_income
    return result

print(solution())