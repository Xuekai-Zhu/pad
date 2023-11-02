def solution():
    """Harold makes $2500.00 a month from his job. His rent is $700.00, his car payment is $300.00, his utilities cost
     1/2 the amount of his car payment and he spends $50.00 on groceries. He wants to put half of the remaining money into a retirement account.
     How much money will that leave him?"""
    monthly_income = 2500
    rent = 700
    car_payment = 300
    utilities = car_payment / 2
    groceries = 50
    total_expenses = rent + car_payment + utilities + groceries
    remaining_money = monthly_income - total_expenses
    retirement_amount = remaining_money / 2
    money_left = remaining_money - retirement_amount
    result = money_left
    return result

print(solution())