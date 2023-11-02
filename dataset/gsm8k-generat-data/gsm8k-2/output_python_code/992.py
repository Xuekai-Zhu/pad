def solution():
    """Rick has 130 cards. He decided to only keep 15 cards and so he gave Miguel some of the cards. 
    Then, he saw 8 friends and decided to give them 12 cards each, and the remaining cards were given 
    equally to his 2 sisters. If each of Rick's sisters got 3 cards, how many cards did Rick give 
    to Miguel?"""
    total_cards = 130
    cards_kept = 15
    cards_given_to_miguel = total_cards - cards_kept
    friends = 8
    cards_per_friend = 12
    cards_given_to_friends = friends * cards_per_friend
    remaining_cards = cards_given_to_miguel - cards_given_to_friends
    cards_per_sister = 3
    cards_given_to_each_sister = cards_per_sister * 2
    total_cards_given = cards_given_to_miguel - remaining_cards - cards_given_to_each_sister
    result = total_cards_given
    return result

print(solution())