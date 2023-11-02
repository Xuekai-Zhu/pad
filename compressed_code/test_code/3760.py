def solution():
    
    total_cards = 16 * 52
    num_layers = 32
    cards_per_layer = total_cards // num_layers
    result = cards_per_layer
    return result

print(solution())