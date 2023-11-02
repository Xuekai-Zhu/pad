def solution():
    """Harold makes $2500.00 a month from his job. His rent is $700.00, his car payment is $300.00, his utilities cost 1/2 the amount of his car payment and he spends $50.00 on groceries. He wants to put half of the remaining money into a retirement account. How much money will that leave him?"""
    # Define Harold's income and expenses
    income = 2500
    rent = 700
    car_payment = 300
    utilities = car_payment / 2
    groceries = 50

    # Calculate Harold's total expenses
    total_expenses = rent + car_payment + utilities + groceries

    # Calculate Harold's remaining money
    remaining_money = income - total_expenses

    # Calculate the amount Harold wants to put into his retirement account
    retirement_amount = remaining_money / 2

    # Calculate the amount of money Harold will have remaining after putting money in his retirement account
    remaining_after_retirement = remaining_money - retirement_amount

    # Display the remaining amount of money
    result = remaining_after_retirement
    return result

print(solution())