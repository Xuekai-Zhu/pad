def solution():
    # Calculate how many cards Joseph gave away to his brother
    given_away = (3/8) * 16 + 2

    # Calculate how many cards Joseph has left
    left = 16 - given_away

    # Calculate the percentage of cards left
    percentage_left = (left/16) * 100
    result = percentage_left
    return result

print(solution())