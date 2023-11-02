def solution():
    """Rick has 130 cards. He decided to only keep 15 cards and so he gave Miguel some of the cards. Then, he saw 8 friends and decided to give them 12 cards each, and the remaining cards were given equally to his 2 sisters. If each of Rick's sisters got 3 cards, how many cards did Rick give to Miguel?"""
    initial_cards = 130
    kept_cards = 15
    miguel_cards = initial_cards - kept_cards
    friends = 8
    cards_per_friend = 12
    total_friend_cards = friends * cards_per_friend
    sisters_cards = 2 * 3
    remaining_cards = initial_cards - kept_cards - miguel_cards - total_friend_cards - sisters_cards
    result = miguel_cards
    
    return result

print(solution())