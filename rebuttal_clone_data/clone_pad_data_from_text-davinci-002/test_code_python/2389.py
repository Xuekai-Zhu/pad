def solution():
    total_cards = 52
    face_cards = 12
    eights = 4
    remaining_cards = total_cards - face_cards - eights
    cards_drawn = 36
    expected_value = (cards_drawn / remaining_cards) * (2/3)
    result = expected_value
    return result

print(solution())