def solution():
    # Calculate Mary's total earnings in a month
    total_earnings = 20 + 40

    # Calculate how much money Mary saves each month
    savings_per_month = 0.5 * total_earnings

    # Calculate how many months it would take Mary to save $150
    months_to_save = 150 / savings_per_month

    result = months_to_save
    return result

print(solution())