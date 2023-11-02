def solution():
    # Find out how many cards Joseph gave to his brother
    cards_given = (3/8) * 16 + 2

    # Find out how many cards are left with Joseph
    cards_left = 16 - cards_given

    # Calculate the percentage of cards left with Joseph
    percentage_left = (cards_left / 16) * 100
    result = percentage_left
    return result

print(solution())