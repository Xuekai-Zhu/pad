def solution():
    # Define the variables
    hourly_rate = 10
    first_month_hours = 35
    second_month_hours = first_month_hours + 5
    total_hours = first_month_hours + second_month_hours
    total_earnings = hourly_rate * total_hours
    personal_spending = 4/5 * total_earnings
    savings = total_earnings - personal_spending

    # Return the savings
    result = savings
    return result

print(solution())