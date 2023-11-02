def solution():
    # Calculate the total number of cards available
    total_cards = 16 * 52

    # Calculate the number of cards per layer
    cards_per_layer = total_cards // 32

    result = cards_per_layer
    return result

print(solution())