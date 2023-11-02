def solution():
    daily_earnings = 40
    tax_rate = 0.1  # 10% tax rate
    num_days = 30

    # Calculate the earnings before taxes for 30 days of work
    earnings_before_tax = daily_earnings * num_days

    # Calculate the amount of taxes Adam will pay for 30 days of work
    taxes_paid = earnings_before_tax * tax_rate

    # Calculate the earnings after taxes for 30 days of work
    earnings_after_tax = earnings_before_tax - taxes_paid
    result = earnings_after_tax
    return result

print(solution())