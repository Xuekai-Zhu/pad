def solution():
    total_cards = 500
    ratio_E_to_O = 11/9

    # Calculate the total number of parts in the ratio
    total_parts = 11 + 9

    # Calculate the number of parts that Ellis gets
    parts_E = 11/total_parts

    # Calculate the number of cards that Ellis gets
    cards_E = parts_E * total_cards

    # Calculate the number of parts that Orion gets
    parts_O = 9/total_parts

    # Calculate the number of cards that Orion gets
    cards_O = parts_O * total_cards

    # Calculate the difference in cards between Ellis and Orion
    cards_diff = cards_E - cards_O
    result = cards_diff
    return result

print(solution())