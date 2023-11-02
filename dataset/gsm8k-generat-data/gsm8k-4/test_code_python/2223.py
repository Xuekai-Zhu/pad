def solution():
    """Elyse had 100 pieces of gum. She gave half to her brother Rick. He gave half of his to his friend Shane. Shane chewed 11 pieces of gum. How many pieces does Shane have left?"""
    # Define the initial number of gum pieces
    gum_pieces = 100

    # Give half to Rick
    gum_pieces = gum_pieces / 2

    # Give half of Rick's gum to Shane
    gum_pieces = gum_pieces / 2

    # Shane chews 11 pieces of gum
    gum_pieces -= 11

    # Display the remaining number of gum pieces Shane has
    result = gum_pieces
    return result

print(solution())