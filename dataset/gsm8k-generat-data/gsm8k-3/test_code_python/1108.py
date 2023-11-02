def solution():
    """Anton has three times as many cards in his collection as Heike does. Ann has six times as many cards as Heike does. If Ann has 60 cards, how many more cards does Ann have more than Anton?"""
    
    # Calculate the number of cards Heike has
    heike_cards = 60 / 6
    
    # Calculate the number of cards Anton has
    anton_cards = heike_cards / 3
    
    # Calculate the difference between the number of cards Ann and Anton have
    ann_anton_diff = 60 - (3 * anton_cards)
    
    # Display the result
    result = ann_anton_diff
    return result

print(solution())