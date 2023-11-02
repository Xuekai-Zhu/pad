def solution():
    """Marcus takes a deck of standard playing cards and takes out all the face cards and the 8's. Mark picks a card at random and then replaces it 36 times. How many times should he expect to pick a card that's both red and has a number divisible by 3?"""
    total_cards = 36
    red_cards = 18
    divisible_by_3 = 6
    favorable_cards = 3
    probability_of_favorable_card = (red_cards/total_cards) * (favorable_cards/divisible_by_3)
    expected_value = probability_of_favorable_card * total_cards
    result = expected_value
    return result

print(solution())