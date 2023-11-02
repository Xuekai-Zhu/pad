def solution():
    """Jed collects stamp cards. Every week, he gets 6 cards. But every two weeks, he gives 2 cards to his friends. If Jed started with 20 cards, after how many weeks will he have a total of 40 cards?"""
    starting_cards = 20
    target_cards = 40
    cards_per_week = 6
    cards_given_away_every_two_weeks = 2
    
    # calculate number of weeks until Jed has target number of cards
    current_cards = starting_cards
    week_count = 0
    
    while current_cards < target_cards:
        week_count += 1
        
        # add 6 cards every week
        current_cards += cards_per_week
        
        # subtract 2 cards every other week
        if week_count % 2 == 0:
            current_cards -= cards_given_away_every_two_weeks
            
    result = week_count
    return result

print(solution())