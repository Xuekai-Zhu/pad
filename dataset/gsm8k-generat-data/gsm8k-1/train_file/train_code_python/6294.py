def solution():
    """Brady gets paid 70 cents for each recipe card he transcribes.
    He also gets a 10 dollar bonus each time he transcribes 100 cards.
    If he transcribes 200 cards how much will he earn including bonuses?"""
    cards_transcribed = 200
    cents_per_card = 70
    bonus_per_100_cards = 10
    total_cents = cards_transcribed * cents_per_card
    bonus_count = cards_transcribed // 100
    total_bonus = bonus_count * bonus_per_100_cards
    total_earnings = total_cents + total_bonus
    result = total_earnings / 100
    
    return result

print(solution())