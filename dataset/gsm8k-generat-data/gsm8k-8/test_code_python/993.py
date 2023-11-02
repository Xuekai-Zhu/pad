def solution():
    # Calculate the number of cards Rick gave to his friends
    friends_cards = 8 * 12

    # Calculate the number of cards Rick kept for himself
    remaining_cards = 130 - 15 - friends_cards

    # Calculate the number of cards given to each sister
    sister_cards = 3 * 2

    # Calculate the number of cards given to Miguel
    miguel_cards = remaining_cards - sister_cards
    result = miguel_cards
    return result

print(solution())