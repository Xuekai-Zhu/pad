def solution():
    # Calculate the total expenses
    total_expenses = 11 + 3 + 16

    # Calculate the hourly expenses for using WiFi
    wifi_expense = 2

    # Calculate the net hourly income
    net_income = 12 - wifi_expense

    # Calculate the required hours to break even
    hours_to_break_even = total_expenses / net_income

    result = hours_to_break_even
    return result

print(solution())