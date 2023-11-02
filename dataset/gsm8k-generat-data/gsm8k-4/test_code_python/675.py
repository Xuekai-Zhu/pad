def solution():
    """Andy is a lawyer who's working on two lawsuits. The first lawsuit has a 30% chance of paying out $5,000,000 upon a win and $0 if he loses it. The second lawsuit has a 50% chance of paying out $1,000,000 if Andy loses and a 50% chance of paying out $2,000,000 if he wins. Expressed as a percentage, how much more likely is it that Andy loses both lawsuits compared to winning both of them?"""
    # Define the possible outcomes of the lawsuits and their probability
    outcomes = [("win", "win"), ("win", "lose"), ("lose", "win"), ("lose", "lose")]
    probabilities = [0.3 * 0.5, 0.3 * 0.5, 0.7 * 0.5, 0.7 * 0.5]

    # Calculate the expected value of each outcome
    values = []
    for outcome in outcomes:
        value = 0
        for i in range(2):
            if outcome[i] == "win":
                if i == 0:
                    value += 5000000
                else:
                    value += 2000000
            else:
                if i == 0:
                    value += 0
                else:
                    value += 1000000
        values.append(value)

    # Calculate the expected value of winning both lawsuits and losing both lawsuits
    win_both = values[0]
    lose_both = values[3]

    # Calculate the probability of winning both lawsuits and losing both lawsuits
    prob_win_both = probabilities[0]
    prob_lose_both = probabilities[3]

    # Calculate the difference in probability
    diff_prob = prob_lose_both - prob_win_both

    # Calculate the percentage difference
    percent_diff = diff_prob / prob_win_both * 100

    result = round(percent_diff, 2)
    return result

print(solution())