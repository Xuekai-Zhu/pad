def solution():
    car_payment = 400  # Ben's car payment is $400
    after_tax_percentage = 0.2  # Ben spends 20% of his after-tax income on his car
    tax_percentage = 1 / 3  # Ben pays 1/3 of his gross income in taxes

    # Calculate Ben's after-tax income
    after_tax_income = car_payment / after_tax_percentage

    # Calculate Ben's gross income
    gross_income = after_tax_income / (1 - tax_percentage)

    # Calculate Ben's monthly income before taxes
    monthly_income_before_tax = gross_income / 12
    result = monthly_income_before_tax
    return result

print(solution())