def solution():
    # Calculate the total number of months in 2 years
    total_months = 2 * 12

    # Calculate the monthly interest rate
    monthly_rate = 10 / 12 / 100

    # Calculate the total amount invested over 2 years
    total_investment = 1000 + (100 * total_months)

    # Calculate the final amount including interest
    final_amount = total_investment * ((1 + monthly_rate) ** total_months)

    result = final_amount
    return result

print(solution())