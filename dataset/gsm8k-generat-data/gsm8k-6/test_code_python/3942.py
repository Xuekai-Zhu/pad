def solution():
    # Calculate the total amount earned by firefighter in a week
    weekly_earning = 30 * 48
    monthly_earning = weekly_earning * 4  # assuming 4 weeks in a month

    # Calculate the total monthly expenses
    rent = monthly_earning / 3
    food = 500
    taxes = 1000
    total_expenses = rent + food + taxes

    # Calculate the remaining amount after paying the expenses
    remaining_amount = monthly_earning - total_expenses
    result = remaining_amount
    return result

print(solution())