def solution():
    # Calculate Adam's earnings after taxes for one day
    earnings_after_tax = 0.9 * 40  # 10% of his money is deducted as taxes

    # Calculate Adam's total earnings after taxes for 30 days of work
    total_earnings_after_tax = earnings_after_tax * 30

    result = total_earnings_after_tax
    return result

print(solution())