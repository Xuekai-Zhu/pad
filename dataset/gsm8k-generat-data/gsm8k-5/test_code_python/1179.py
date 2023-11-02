def solution():
    # Calculate the number of doubles Rob has
    doubles_rob = 40 / 5  # Jess has 5 times as many doubles as Rob, so Rob has 1/5 of the doubles Jess has
    # Therefore, Rob has 1/3 of his total cards as doubles, so the total number of cards he has is 3 times the number of doubles he has
    total_cards_rob = doubles_rob * 3

    result = total_cards_rob
    return result

print(solution())