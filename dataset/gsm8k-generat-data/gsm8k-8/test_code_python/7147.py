def solution():
    # Define the starting number of cards, the number of cards gained per week, and the number of cards lost every two weeks
    starting_cards = 20
    cards_per_week = 6
    cards_lost_every_two_weeks = 2

    # Keep track of the number of weeks and total number of cards at each week
    week = 0
    total_cards = starting_cards

    while total_cards < 40:
        week += 1
        total_cards += cards_per_week
        
        # Every two weeks, subtract 2 cards
        if week % 2 == 0:
            total_cards -= cards_lost_every_two_weeks

    result = week
    return result

print(solution())