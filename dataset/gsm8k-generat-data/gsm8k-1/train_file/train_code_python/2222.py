def solution():
    """Elyse had 100 pieces of gum. She gave half to her brother Rick. He gave half of his to his friend Shane. Shane chewed 11 pieces of gum. How many pieces does Shane have left?"""
    initial_gum = 100
    rick_gum = initial_gum / 2
    shane_gum = rick_gum / 2
    shane_gum -= 11
    result = shane_gum
    return result

print(solution())