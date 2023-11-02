def solution():
    """John is holding a poker night with his friends and is getting the decks of cards ready before his friends show up. After losing so many cards from various decks, John thinks he needs to count exactly how many cards he has to make sure he has enough full decks for the night. Each deck of cards should hold 52 cards. He finds 3 half-full decks of cards and 3 full decks of cards. As he is arranging them, he realizes that the quality of a lot of the cards is quite poor and decides to throw 34 of the cards in the trash. How many cards does John now have?"""
    # Define the number of full decks and half-full decks
    full_decks = 3
    half_decks = 3

    # Calculate the total number of cards before throwing any away
    total_cards = (full_decks * 52) + (half_decks * 26)

    # Calculate the total number of cards after throwing away 34 cards
    total_cards = total_cards - 34

    result = total_cards
    return result

print(solution())