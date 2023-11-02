def solution():
    """Nicole collected 400 Pokemon cards. Cindy collected twice as many, and Rex collected half of Nicole and Cindy's combined total. 
    If Rex divided his card equally among himself and his three younger siblings, how many cards does Rex have left?"""
    
    # Define the number of cards collected by Nicole and Cindy 
    nicole_cards = 400
    cindy_cards = nicole_cards * 2
    
    # Calculate the combined total of Nicole and Cindy's cards 
    total_cards = nicole_cards + cindy_cards
    
    # Calculate the number of cards collected by Rex 
    rex_cards = total_cards / 2
    
    # Calculate the total number of siblings Rex divided his cards with 
    total_siblings = 3 + 1 # Rex + 3 younger siblings
    
    # Calculate the number of cards each sibling gets
    cards_per_sibling = rex_cards / total_siblings
    
    # Calculate the number of cards left with Rex 
    cards_left = rex_cards - (cards_per_sibling * total_siblings)
    
    result = cards_left
    return result

print(solution())