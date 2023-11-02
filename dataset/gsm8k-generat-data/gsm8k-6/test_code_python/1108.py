def solution():
    # Calculate the number of cards Heike has
    heike_cards = 60 / 6

    # Calculate the number of cards Anton has
    anton_cards = heike_cards / 3

    # Calculate the difference in cards between Ann and Anton
    difference = 60 - anton_cards

    result = difference
    return result

print(solution())