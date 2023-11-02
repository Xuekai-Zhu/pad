def solution():
    """On Monday Buddy has 30 baseball cards. On Tuesday Buddy loses half of them. On Wednesday Buddy buys 12 baseball cards. On Thursday he buys a third of what he had on Tuesday. How many baseball cards does he have on Thursday?"""
    monday_cards = 30
    tuesday_cards = monday_cards / 2
    wednesday_cards = monday_cards + 12
    thursday_cards = (tuesday_cards / 3) + wednesday_cards
    result = thursday_cards
    return result

print(solution())