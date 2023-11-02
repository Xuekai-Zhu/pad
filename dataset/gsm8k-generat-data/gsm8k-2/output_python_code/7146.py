def solution():
    """Jed collects stamp cards. Every week, he gets 6 cards. But every two weeks, he gives 2 cards to his friends. If Jed started with 20 cards, after how many weeks will he have a total of 40 cards?"""
    jed_cards = 20
    target_cards = 40
    weekly_cards = 6
    gift_cards = 2
    weeks = 0
    while jed_cards < target_cards:
        weeks += 1
        jed_cards += weekly_cards
        if weeks % 2 == 0:
            jed_cards -= gift_cards
    result = weeks
    return result

print(solution())