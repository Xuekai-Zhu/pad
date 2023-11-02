def solution():
    ann_cards = 60  # Ann has 60 cards
    heike_cards = ann_cards / 6  # Heike has one-sixth the number of cards that Ann has
    anton_cards = heike_cards / 3  # Anton has one-third the number of cards that Heike has

    # Calculate the difference in the number of cards between Ann and Anton
    difference = ann_cards - anton_cards
    result = difference
    return result

print(solution())