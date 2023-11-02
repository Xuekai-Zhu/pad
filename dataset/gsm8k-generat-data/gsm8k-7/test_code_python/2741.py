def solution():
    total_cost = 485
    grandma_contribution = 250
    money_to_earn = total_cost - grandma_contribution
    earnings_per_bar = 1.25

    # Calculate the number of candy bars Zoe needs to sell to earn the remaining money
    num_bars_to_sell = money_to_earn / earnings_per_bar
    result = num_bars_to_sell
    return result

print(solution())