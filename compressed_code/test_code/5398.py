def solution():
    
    hockey_cards = 200
    football_cards = 4 * hockey_cards
    baseball_cards = football_cards - 50
    total_cards = hockey_cards + football_cards + baseball_cards
    result = total_cards
    return result

print(solution())