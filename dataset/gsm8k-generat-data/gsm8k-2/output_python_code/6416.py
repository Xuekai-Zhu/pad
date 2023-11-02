def solution():
    """Harold makes $2500.00 a month from his job. His rent is $700.00, his car payment is $300.00, his utilities cost 1/2 the amount of his car payment and he spends $50.00 on groceries. He wants to put half of the remaining money into a retirement account. How much money will that leave him?"""
    total_income = 2500
    rent = 700
    car_payment = 300
    utilities = car_payment / 2
    groceries = 50
    total_expenses = rent + car_payment + utilities + groceries
    remaining_income = total_income - total_expenses
    retirement_savings = remaining_income / 2
    remaining_money = remaining_income - retirement_savings
    result = remaining_money
    return result

print(solution())