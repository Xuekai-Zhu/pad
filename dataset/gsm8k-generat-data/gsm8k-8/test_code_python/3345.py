def solution():
    # Determine Rica's share of the prize money
    total_prize_money = 8/3 * 300
    rica_share = 3/8 * total_prize_money

    # Calculate how much Rica spent
    rica_spent = rica_share * 1/5

    # Determine how much prize money her group won
    group_prize_money = total_prize_money / (3/8)

    result = group_prize_money
    return result

print(solution())