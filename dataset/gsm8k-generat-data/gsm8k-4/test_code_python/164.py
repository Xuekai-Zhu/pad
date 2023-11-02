def solution():
    """On Monday Buddy has 30 baseball cards. On Tuesday Buddy loses half of them. 
    On Wednesday Buddy buys 12 baseball cards. 
    On Thursday he buys a third of what he had on Tuesday. How many baseball cards does he have on Thursday?"""
    
    # Buddy starts with 30 baseball cards on Monday
    monday_cards = 30
    
    # On Tuesday, he loses half of them
    tuesday_cards = monday_cards / 2
    
    # On Wednesday, he buys 12 baseball cards
    wednesday_cards = tuesday_cards + 12
    
    # On Thursday, he buys a third of what he had on Tuesday
    thursday_cards = tuesday_cards / 3
    
    # Total number of cards on Thursday
    total_cards = thursday_cards + wednesday_cards
    
    result = total_cards
    return result

print(solution())