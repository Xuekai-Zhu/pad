def solution():
    """Andy is a lawyer who's working on two lawsuits. The first lawsuit has a 30% chance of paying out $5,000,000 upon a win and $0 if he loses it. The second lawsuit has a 50% chance of paying out $1,000,000 if Andy loses and a 50% chance of paying out $2,000,000 if he wins.
    Expressed as a percentage, how much more likely is it that Andy loses both lawsuits compared to winning both of them?"""
    lawsuit1_win_prob = 0.3
    lawsuit1_win_payoff = 5000000
    lawsuit2_win_prob = 0.5
    lawsuit2_win_payoff = 2000000
    lawsuit2_lose_payoff = 1000000

    # probability of winning both lawsuits
    win_both = lawsuit1_win_prob * (lawsuit2_win_prob * lawsuit2_win_payoff + (1 - lawsuit2_win_prob) * lawsuit2_lose_payoff)

    # probability of losing both lawsuits
    lose_both = (1 - lawsuit1_win_prob) * (lawsuit2_win_prob * lawsuit2_lose_payoff + (1 - lawsuit2_win_prob) * 0)

    # difference in likelihood between losing both and winning both
    difference = (lose_both - win_both) * 100

    result = difference
    return result

print(solution())