def solution():
    # Calculate the cost of fixing the racecar after the discount
    cost = 20000 * 0.8  # 20% discount means he pays only 80% of the cost

    # Calculate the winnings from the race after the 10% deduction
    winnings = 70000 * 0.9  # 10% deduction means he keeps only 90% of the prize money

    # Calculate John's profits from the racecar
    profits = winnings - cost
    result = profits
    return result

print(solution())