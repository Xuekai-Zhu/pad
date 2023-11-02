def solution():
    raffle_winnings = 100  # Tim won a $100 raffle
    percentage_given_away = 0.2  # Tim gave away 20% of his winnings

    # Calculate the amount given away to his friend
    amount_given_away = raffle_winnings * percentage_given_away

    # Calculate the amount Tim kept for himself
    amount_kept = raffle_winnings - amount_given_away
    result = amount_kept
    return result

print(solution())