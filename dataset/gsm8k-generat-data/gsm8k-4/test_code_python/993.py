def solution():
    """Rick has 130 cards. He decided to only keep 15 cards and so he gave Miguel some of the cards. Then, he saw 8 friends and decided to give them 12 cards each, and the remaining cards were given equally to his 2 sisters. If each of Rick's sisters got 3 cards, how many cards did Rick give to Miguel?"""
    # Define the initial number of cards
    initial_cards = 130
    
    # Define the number of cards Rick kept
    rick_cards = 15
    
    # Calculate the number of cards given to Miguel
    miguel_cards = initial_cards - rick_cards
    
    # Calculate the number of cards given to the friends
    friend_cards = 12 * 8
    
    # Calculate the number of cards given to Rick's sisters
    sister_cards = (initial_cards - rick_cards - friend_cards) / 2
    
    # Calculate the number of cards given to Miguel
    miguel_cards = initial_cards - rick_cards - friend_cards - sister_cards
    
    result = miguel_cards
    return result

print(solution())