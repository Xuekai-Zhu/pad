def solution():
    # Calculate the amount of money Opal put into savings
    first_savings = 100 / 2  # half of $100 winnings
    bet = 100 / 2  # other half of winnings
    second_savings = (bet * 0.6) / 2  # 60% profit on bet, half put into savings
    total_savings = first_savings + second_savings  # total amount saved
    result = total_savings
    return result

print(solution())