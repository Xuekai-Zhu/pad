def solution():
    
    total_cards = 365
    brother_sets = 8
    sister_sets = 5
    friend_sets = 2
    cards_per_set = 13
    total_given_away = (brother_sets + sister_sets + friend_sets) * cards_per_set
    result = total_given_away
    return result

print(solution())