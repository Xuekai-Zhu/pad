def solution():
    # Calculate the total earnings of Alice for the month
    total_earnings = 2500 + 240 + (0.02 * 2500)  # $2500 worth of sales + $240 basic salary + 2% commission

    # Calculate the amount Alice will save
    amount_saved = 0.1 * total_earnings  # 10% of total earnings

    result = amount_saved
    return result

print(solution())