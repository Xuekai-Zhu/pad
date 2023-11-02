def solution():
    """Harold makes $2500.00 a month from his job. His rent is $700.00, his car payment is $300.00, his utilities cost 1/2 the amount of his car payment and he spends $50.00 on groceries.
    He wants to put half of the remaining money into a retirement account. How much money will that leave him?"""
    # Define the amounts of rent, car payment, utilities, and groceries
    rent = 700
    car_payment = 300
    utilities = car_payment / 2
    groceries = 50

    # Calculate the total monthly expenses
    total_expenses = rent + car_payment + utilities + groceries

    # Calculate the remaining money after paying the expenses
    remaining_money = 2500 - total_expenses

    # Calculate the amount of money to put into a retirement account
    retirement_fund = remaining_money / 2

    # Calculate the final amount of money remaining after putting half into a retirement account
    final_money = remaining_money - retirement_fund

    # return the result
    result = final_money
    return result

print(solution())