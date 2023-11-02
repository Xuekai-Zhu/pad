def solution():
    """Brady gets paid 70 cents for each recipe card he transcribes. He also gets a 10 dollar bonus each time he transcribes 100 cards. If he transcribes 200 cards how much will he earn including bonuses?"""
    # Define the payment for each recipe card
    CARD_PAYMENT = 0.70

    # Define the bonus payment for every 100 cards
    BONUS_PAYMENT = 10

    # Determine the number of 100-card sets Brady transcribed
    sets_transcribed = 200 // 100

    # Determine the remaining number of cards transcribed
    cards_transcribed = 200 % 100

    # Calculate the earnings from transcribing the 100-card sets
    set_earnings = sets_transcribed * BONUS_PAYMENT

    # Calculate the earnings from transcribing the remaining cards
    card_earnings = cards_transcribed * CARD_PAYMENT

    # Calculate the total earnings
    total_earnings = set_earnings + card_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())