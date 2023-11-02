def solution():
    """Elyse had 100 pieces of gum. She gave half to her brother Rick. He gave half of his to his friend Shane. Shane chewed 11 pieces of gum. How many pieces does Shane have left?"""
    # Define the initial number of gum pieces
    initial_pieces = 100

    # Elyse gives half of the gum pieces to Rick
    rick_pieces = initial_pieces // 2

    # Rick gives half of his pieces to Shane
    shane_pieces = rick_pieces // 2

    # Shane chews some pieces
    shane_pieces -= 11

    # Display the number of pieces Shane has left
    result = shane_pieces
    return result

print(solution())