def solution():
    hourly_rate = 12.5
    hours_worked = 40
    tax_rate = 0.2
    gummy_bear_rate = 0.15

    # Calculate Paul's gross income
    gross_income = hourly_rate * hours_worked

    # Calculate Paul's net income after taxes and fees
    net_income = gross_income * (1 - tax_rate)

    # Calculate how much Paul spends on gummy bears
    gummy_bear_spending = net_income * gummy_bear_rate

    # Calculate how much Paul has left after gummy bear spending
    remaining_income = net_income - gummy_bear_spending
    result = remaining_income
    return result

print(solution())