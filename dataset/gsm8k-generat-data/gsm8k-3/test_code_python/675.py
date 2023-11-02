def solution():
    """Andy is a lawyer who's working on two lawsuits. The first lawsuit has a 30% chance of paying out $5,000,000 upon a win and $0 if he loses it. The second lawsuit has a 50% chance of paying out $1,000,000 if Andy loses and a 50% chance of paying out $2,000,000 if he wins. Expressed as a percentage, how much more likely is it that Andy loses both lawsuits compared to winning both of them?"""
    # Calculate the probabilities of each outcome for the first lawsuit
    p_win_1 = 0.3
    p_loss_1 = 0.7
    payout_win_1 = 5000000
    payout_loss_1 = 0

    # Calculate the probabilities of each outcome for the second lawsuit
    p_win_2 = 0.5
    p_loss_2 = 0.5
    payout_win_2 = 2000000
    payout_loss_2 = 1000000

    # Calculate the expected value of each outcome for each lawsuit
    ev_win_1 = p_win_1 * payout_win_1
    ev_loss_1 = p_loss_1 * payout_loss_1
    ev_win_2 = p_win_2 * payout_win_2
    ev_loss_2 = p_loss_2 * payout_loss_2

    # Calculate the expected value of winning or losing both lawsuits
    ev_win_both = ev_win_1 * ev_win_2
    ev_loss_both = ev_loss_1 * ev_loss_2

    # Calculate the probability of winning or losing both lawsuits
    p_win_both = p_win_1 * p_win_2
    p_loss_both = p_loss_1 * p_loss_2

    # Calculate the difference in probabilities between losing both and winning both
    likelihood_diff = (p_loss_both - p_win_both) * 100

    # Display the difference in likelihoods as a percentage
    result = likelihood_diff
    return result

print(solution())