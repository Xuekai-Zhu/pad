def solution():
    # Total number of cards after removing face cards and 8's
    total_cards = 36

    # Number of red cards divisible by 3
    red_divisible_three = 2

    # Probability of picking a red divisible by 3 card
    prob_red_divisible_three = red_divisible_three / total_cards

    # Expected number of times to pick a red divisible by 3 card in 36 picks
    expected_picks = prob_red_divisible_three * 36

    result = expected_picks
    return result

print(solution())