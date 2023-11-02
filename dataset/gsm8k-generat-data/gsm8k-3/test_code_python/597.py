def solution():
    """John is holding a poker night with his friends and is getting the decks of cards ready before his friends show up. After losing so many cards from various decks, John thinks he needs to count exactly how many cards he has to make sure he has enough full decks for the night. Each deck of cards should hold 52 cards. He finds 3 half-full decks of cards and 3 full decks of cards. As he is arranging them, he realizes that the quality of a lot of the cards is quite poor and decides to throw 34 of the cards in the trash. How many cards does John now have?"""
    # Define the number of cards in a full deck
    FULL_DECK = 52

    # Define the number of half-full decks and full decks John has
    half_full_decks = 3
    full_decks = 3

    # Calculate the total number of cards John has before throwing any away
    total_cards = (half_full_decks * FULL_DECK) + (full_decks * FULL_DECK)

    # Subtract the number of cards John throws away
    total_cards -= 34

    # Display the total number of cards John has
    result = total_cards
    return result

print(solution())