def solution():
    
    original_cards = 16
    given_to_brother = (3/8)*original_cards + 2
    cards_left = original_cards - given_to_brother
    percentage_left = (cards_left/original_cards) * 100
    result = percentage_left
    return result

print(solution())