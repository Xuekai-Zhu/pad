def solution():
    """Brady gets paid 70 cents for each recipe card he transcribes. He also gets a 10 dollar bonus each time he transcribes 100 cards. If he transcribes 200 cards how much will he earn including bonuses?"""
    # Define the payment per recipe card and the bonus amount
    PAYMENT_PER_CARD = 0.7
    BONUS_AMOUNT = 10

    # Define the total number of recipe cards to be transcribed
    TOTAL_CARDS = 200

    # Calculate the total payment for transcribing all the cards
    total_payment = PAYMENT_PER_CARD * TOTAL_CARDS

    # Calculate the number of bonuses to be received
    num_bonuses = TOTAL_CARDS // 100

    # Calculate the total bonus amount to be received
    total_bonus = num_bonuses * BONUS_AMOUNT

    # Add the bonus amount to the total payment
    total_earnings = total_payment + total_bonus
    
    result = total_earnings
    return result

print(solution())