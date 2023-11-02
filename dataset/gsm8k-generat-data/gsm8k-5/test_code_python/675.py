def solution():
    # Calculate the probability of winning the first lawsuit
    probability_lawsuit1_win = 0.3

    # Calculate the probability of winning the second lawsuit
    probability_lawsuit2_win = 0.5 * 0.5 + 0.5 * 0.5

    # Calculate the probability of losing both lawsuits
    probability_both_lose = (1 - probability_lawsuit1_win) * (1 - probability_lawsuit2_win)

    # Calculate the probability of winning both lawsuits
    probability_both_win = probability_lawsuit1_win * 0.5

    # Calculate the difference in probabilities as a percentage
    difference = (probability_both_lose - probability_both_win) * 100

    result = difference
    return result

print(solution())