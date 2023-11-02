def solution():
    total_cards = 36
    red_cards = 26  # 26 out of 36 cards are red
    divisible_by_3_cards = 12  # there are 12 cards from 2 to 10 that are divisible by 3

    # Calculate the probability of picking a red card and a card divisible by 3
    probability = (red_cards / total_cards) * (divisible_by_3_cards / total_cards)

    # Calculate the expected number of times Mark will pick a red card that's divisible by 3
    expected_times = probability * total_cards
    result = round(expected_times)
    return result

print(solution())