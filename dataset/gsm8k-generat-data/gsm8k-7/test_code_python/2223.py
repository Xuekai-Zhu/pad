def solution():
    initial_pieces = 100

    # Elyse gives half of her gum to Rick
    elyse_remaining = initial_pieces / 2
    rick_received = initial_pieces / 2

    # Rick gives half of his gum to Shane
    rick_remaining = rick_received / 2
    shane_received = rick_received / 2

    # Shane chews 11 pieces of gum
    shane_remaining = shane_received - 11

    result = shane_remaining
    return result

print(solution())