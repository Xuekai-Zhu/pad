def solution():
    brandon_cards = 20
    malcom_cards = brandon_cards + 8
    malcom_cards_after_transfer = malcom_cards / 2
    malcom_cards_left = malcom_cards - malcom_cards_after_transfer
    result = malcom_cards_left
    return result

print(solution())