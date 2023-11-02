def solution():
    # Calculate the probability of winning and losing the first lawsuit
    prob_win_lawsuit1 = 0.3
    prob_lose_lawsuit1 = 0.7

    # Calculate the probability of winning and losing the second lawsuit
    prob_win_lawsuit2 = 0.5
    prob_lose_lawsuit2 = 0.5

    # Calculate the probability of winning both lawsuits
    prob_win_both = prob_win_lawsuit1 * prob_win_lawsuit2

    # Calculate the probability of losing both lawsuits
    prob_lose_both = prob_lose_lawsuit1 * prob_lose_lawsuit2

    # Calculate the difference in probability between losing both and winning both
    diff_prob = (prob_lose_both - prob_win_both) * 100

    result = diff_prob
    return result

print(solution())