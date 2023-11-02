def solution():
    brandon_cards = 20 # Brandon has 20 baseball cards
    malcom_cards = brandon_cards + 8 # Malcom has 8 more cards than Brandon
    malcom_cards = malcom_cards - (malcom_cards // 2) # Malcom gives half of his cards to Mark
    result = malcom_cards
    return result

print(solution())