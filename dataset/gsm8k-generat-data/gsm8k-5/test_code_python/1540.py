def solution():
    principal = 10000  # Sam invested $10,000 initially
    rate = 0.2  # 20% interest compounded annually
    time = 3  # Invested for 3 years
    amount = principal * ((1 + rate) ** time)  # Calculate the amount after 3 years

    # Calculate the amount Sam needs to invest to have three times as much
    target_amount = 3 * amount
    remaining_amount = target_amount - principal
    remaining_years = 1  # Invested for 1 more year
    required_rate = ((target_amount / principal) ** (1 / remaining_years)) - 1
    additional_investment = remaining_amount / ((1 + required_rate) ** remaining_years)

    # Calculate the total investment and return after the next year
    total_investment = principal + additional_investment
    rate = 0.15  # 15% return in the next year
    time = 1  # Invested for 1 more year
    total_amount = total_investment * ((1 + rate) ** time)

    result = total_amount
    return result

print(solution())