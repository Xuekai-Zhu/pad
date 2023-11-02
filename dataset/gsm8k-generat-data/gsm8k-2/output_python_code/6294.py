def solution():
    """Brady gets paid 70 cents for each recipe card he transcribes. He also gets a 10 dollar bonus each time he transcribes 100 cards. If he transcribes 200 cards how much will he earn including bonuses?"""
    pay_per_card = 0.7
    bonus_per_100_cards = 10
    cards_to_transcribe = 200

    # Calculate pay for transcribing 200 cards
    base_pay = pay_per_card * cards_to_transcribe

    # Calculate number of 100-card sets completed and apply bonus
    bonus_sets = cards_to_transcribe // 100
    bonus_pay = bonus_sets * bonus_per_100_cards

    # Calculate total pay including bonuses
    total_pay = base_pay + bonus_pay

    # Convert to dollar format
    result = "${:.2f}".format(total_pay)
    return result

print(solution())