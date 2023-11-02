def solution():
    """On Monday Buddy has 30 baseball cards. On Tuesday Buddy loses half of them. On Wednesday Buddy buys 12 baseball cards. On Thursday he buys a third of what he had on Tuesday. How many baseball cards does he have on Thursday?"""
    monday_cards = 30
    tuesday_cards = monday_cards / 2
    wednesday_cards = tuesday_cards + 12
    thursday_cards = tuesday_cards / 3
    total_cards = monday_cards + tuesday_cards + wednesday_cards + thursday_cards
    result = total_cards
    return result

print(solution())