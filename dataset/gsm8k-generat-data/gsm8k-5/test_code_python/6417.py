def solution():
    monthly_income = 2500.00  # Harold makes $2500.00 a month
    rent = 700.00  # His rent is $700.00
    car_payment = 300.00  # His car payment is $300.00
    utilities = car_payment/2  # His utilities cost is 1/2 the amount of his car payment
    groceries = 50.00  # He spends $50.00 on groceries
    expenses = rent + car_payment + utilities + groceries  # Total expenses
    remaining_income = monthly_income - expenses  # Remaining income after expenses
    retirement_savings = remaining_income / 2  # Half of the remaining income goes to retirement savings
    money_left = remaining_income - retirement_savings  # Money left after retirement savings
    result = money_left
    return result

print(solution())