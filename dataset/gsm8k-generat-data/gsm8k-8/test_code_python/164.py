def solution():
    # Calculate how many baseball cards Buddy has on Tuesday
    tuesday_cards = 30 / 2

    # Calculate how many baseball cards he has after buying more on Wednesday
    wednesday_cards = tuesday_cards + 12

    # Calculate how many he buys on Thursday
    thursday_cards = tuesday_cards / 3

    # Calculate the total number of cards he has on Thursday
    total_cards = wednesday_cards + thursday_cards
    result = total_cards
    return result

print(solution())