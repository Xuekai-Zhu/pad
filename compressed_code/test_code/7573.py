def solution():
    
    initial_cards = 52
    extra_cards = 2
    total_cards = initial_cards + extra_cards
    players = 3
    cards_per_player = total_cards // players
    result = cards_per_player
    return result

print(solution())