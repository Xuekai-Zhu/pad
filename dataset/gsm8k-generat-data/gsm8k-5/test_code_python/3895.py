def solution():
    num_cards_given = (3/8)*16 + 2  # Joseph gave 3/8 of his cards and 2 cards to his brother
    num_cards_left = 16 - num_cards_given  # Calculate the number of cards left to Joseph

    # Calculate the percentage of cards left to Joseph
    percentage_left = (num_cards_left/16)*100
    result = percentage_left
    return result

print(solution())