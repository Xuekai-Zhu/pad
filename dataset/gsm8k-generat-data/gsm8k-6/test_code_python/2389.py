def solution():
    # Calculate the number of eligible cards in the deck
    eligible_cards = 2 * 4 * 3  # 2 red suits, 4 numbers per suit, 3 numbers divisible by 3 per suit

    # Calculate the probability of picking an eligible card
    prob_eligible_card = eligible_cards / 36

    # Calculate the expected number of times to pick an eligible card
    expected_times = prob_eligible_card * 36

    result = expected_times
    return result

print(solution())