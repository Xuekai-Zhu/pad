def solution():
    monthly_income = 2500
    rent = 700
    car_payment = 300
    utilities = car_payment / 2
    groceries = 50

    # Calculate the total amount of expenses
    total_expenses = rent + car_payment + utilities + groceries

    # Calculate the total amount of money left after expenses
    total_leftover = monthly_income - total_expenses

    # Calculate the amount of money Harold wants to put into his retirement account
    retirement_amount = total_leftover / 2

    # Calculate the total amount of money left after putting money into retirement account
    total_left_after_retirement = total_leftover - retirement_amount
    result = total_left_after_retirement
    return result

print(solution())