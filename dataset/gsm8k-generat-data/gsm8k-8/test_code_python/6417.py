def solution():
    # Define the given values
    monthly_income = 2500
    rent = 700
    car_payment = 300
    utilities = car_payment / 2
    groceries = 50

    # Calculate the total expenses
    total_expenses = rent + car_payment + utilities + groceries

    # Calculate the remaining money
    remaining_money = monthly_income - total_expenses

    # Calculate the amount to put into retirement account
    retirement_amount = remaining_money / 2

    # Calculate the final remaining money
    final_remaining_money = remaining_money - retirement_amount
    result = final_remaining_money
    return result

print(solution())