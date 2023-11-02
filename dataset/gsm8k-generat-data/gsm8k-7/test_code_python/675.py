def solution():
    lawsuit1_win = 0.3
    lawsuit1_payoff = 5000000
    lawsuit2_win = 0.5
    lawsuit2_loss_payoff = 1000000
    lawsuit2_win_payoff = 2000000

    # Calculate the expected value of lawsuit 1
    lawsuit1_value = lawsuit1_win * lawsuit1_payoff

    # Calculate the expected payoff of lawsuit 2 if Andy wins
    lawsuit2_win_value = lawsuit2_win * lawsuit2_win_payoff

    # Calculate the expected payoff of lawsuit 2 if Andy loses
    lawsuit2_loss_value = (1 - lawsuit2_win) * lawsuit2_loss_payoff

    # Calculate the expected value of lawsuit 2
    lawsuit2_value = lawsuit2_win_value + lawsuit2_loss_value

    # Calculate the probability of losing both lawsuits
    lose_both_prob = (1 - lawsuit1_win) * (1 - lawsuit2_win)

    # Calculate the probability of winning both lawsuits
    win_both_prob = lawsuit1_win * lawsuit2_win

    # Calculate the difference in probabilities between losing and winning both lawsuits
    prob_difference = lose_both_prob - win_both_prob

    # Convert to a percentage
    result = prob_difference * 100
    return result

print(solution())