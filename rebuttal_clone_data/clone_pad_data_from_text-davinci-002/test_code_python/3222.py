def solution():
    cards_collected = 400
    cindys_cards = cards_collected * 2
    rexs_cards = (cards_collected + cindys_cards) / 2
    rex_divided = rexs_cards / 4
    rex_leftover = rexs_cards - rex_divided
    result = rex_leftover
    
    return result

print(solution())