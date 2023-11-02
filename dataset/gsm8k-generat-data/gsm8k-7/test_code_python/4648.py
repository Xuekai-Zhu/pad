def solution():
    earnings_per_customer = 18
    monthly_expenses = 280
    recreation_percentage = 0.2
    num_customers = 80

    # Calculate the total earnings for the month
    total_earnings = earnings_per_customer * num_customers

    # Calculate the recreation and relaxation expenses for the month
    recreation_expenses = total_earnings * recreation_percentage

    # Calculate the total expenses for the month
    total_expenses = monthly_expenses + recreation_expenses

    # Calculate the savings for the month
    savings = total_earnings - total_expenses
    result = savings
    return result

print(solution())