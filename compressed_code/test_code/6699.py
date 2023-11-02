def solution():
    
    basketball_boxes = 4
    basketball_cards_per_box = 10
    baseball_boxes = 5
    baseball_cards_per_box = 8
    total_basketball_cards = basketball_boxes * basketball_cards_per_box
    total_baseball_cards = baseball_boxes * baseball_cards_per_box
    total_cards = total_basketball_cards + total_baseball_cards
    cards_given_away = 58
    cards_left = total_cards - cards_given_away
    result = cards_left
    return result

print(solution())