def solution():
    daily_earnings = 40  # Adam earns $40 daily
    tax_rate = 0.1  # 10% of his money is deducted as taxes
    days_worked = 30  # Adam works for 30 days

    # Calculate Adam's earnings after taxes for one day
    earnings_after_tax = daily_earnings * (1 - tax_rate)

    # Calculate Adam's total earnings after taxes
    total_earnings = earnings_after_tax * days_worked
    result = total_earnings
    return result

print(solution())