def solution():
    # Calculate the probability of winning or losing the first lawsuit
    prob_first_win = 0.3
    prob_first_lose = 0.7

    # Calculate the probability of winning or losing the second lawsuit
    prob_second_win = 0.5
    prob_second_lose = 0.5

    # Calculate the probability of winning or losing both lawsuits
    prob_both_win = prob_first_win * prob_second_win
    prob_both_lose = prob_first_lose * prob_second_lose

    # Calculate the difference in probability between losing both and winning both
    prob_diff = (prob_both_lose - prob_both_win) * 100
    result = prob_diff
    return result

print(solution())