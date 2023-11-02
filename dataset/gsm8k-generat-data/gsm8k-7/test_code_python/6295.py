def solution():
    card_rate = 0.70
    bonus_rate = 10.00
    bonus_cards = 100
    total_cards = 200

    # Calculate the number of bonuses earned
    num_bonuses = total_cards // bonus_cards

    # Calculate the total earnings from card transcription
    card_earnings = total_cards * card_rate

    # Calculate the total earnings from bonuses
    bonus_earnings = num_bonuses * bonus_rate

    # Calculate the total earnings, including bonuses
    total_earnings = card_earnings + bonus_earnings
    result = total_earnings
    return result

print(solution())