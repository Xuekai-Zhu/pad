def solution():
    # Calculate Harold's total expenses
    total_expenses = 700 + 300 + (1/2)*300 + 50  # rent + car payment + utilities + groceries

    # Calculate Harold's remaining money
    remaining_money = 2500 - total_expenses

    # Calculate the amount of money Harold will put in his retirement account
    retirement_money = remaining_money / 2

    # Calculate the money Harold will have after putting money in his retirement account
    remaining_money = remaining_money - retirement_money

    result = remaining_money
    return result

print(solution())