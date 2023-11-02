def solution():
    # Calculate the total number of shirts made per day
    shirts_per_day = 20 * 20

    # Calculate the total amount earned from selling shirts
    total_sales = shirts_per_day * 35

    # Calculate the total amount paid in employee wages
    total_wages = 20 * 12 * 8 + shirts_per_day * 5

    # Calculate the total expenses
    total_expenses = total_wages + 1000

    # Calculate the daily profits
    daily_profits = total_sales - total_expenses
    result = daily_profits
    return result

print(solution())