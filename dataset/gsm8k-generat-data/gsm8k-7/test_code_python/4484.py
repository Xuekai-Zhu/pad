def solution():
    paycheck = 5000
    expenses = 4600
    months_in_year = 12

    # Calculate the total amount of money Diego has to save per month
    savings_per_month = paycheck - expenses

    # Calculate the total amount of savings over the course of a year
    total_savings = savings_per_month * months_in_year
    result = total_savings
    return result

print(solution())