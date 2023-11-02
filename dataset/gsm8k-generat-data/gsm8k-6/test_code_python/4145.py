def solution():
    car_payment = 400  # Ben's car payment
    tax_rate = 1/3  # Ben pays 1/3 of his gross income in taxes
    car_budget_percent = 20/100  # Ben spends 20% of his after-tax income on his car

    # Calculate how much of Ben's income is available for his car payment
    after_tax_income = car_payment / car_budget_percent

    # Calculate Ben's gross income
    gross_income = after_tax_income / (1 - tax_rate)
    result = gross_income
    return result

print(solution())