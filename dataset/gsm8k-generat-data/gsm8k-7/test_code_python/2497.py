def solution():
    raffle_win = 100
    friend_share = 0.2  # 20% share given to friend

    # Calculate the amount that Tim gave away to his friend
    amount_given_away = raffle_win * friend_share

    # Calculate the amount that Tim kept for himself
    amount_kept = raffle_win - amount_given_away
    result = amount_kept
    return result

print(solution())