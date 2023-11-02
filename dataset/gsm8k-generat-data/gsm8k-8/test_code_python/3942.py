def solution():
    # Calculate the firefighter's total earnings per week
    weekly_earnings = 30 * 48

    # Calculate the firefighter's total earnings per month
    monthly_earnings = weekly_earnings * 4

    # Calculate the amount of money paid on rent per month
    rent = monthly_earnings / 3

    # Calculate the total amount spent on expenses per month
    total_expenses = rent + 500 + 1000

    # Calculate the amount of money the firefighter has after paying monthly expenses
    money_left = monthly_earnings - total_expenses
    result = money_left
    return result

print(solution())