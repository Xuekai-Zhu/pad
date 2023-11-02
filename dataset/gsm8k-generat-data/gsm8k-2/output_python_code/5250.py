def solution():
    """Donna made a cake to take to a party where the guests ate half the cake. The day after the party, she shared half the leftovers with her brothers. The following day, she ate one piece as a midnight snack. Twice as many pieces as her snack were left. How many pieces was the cake to begin with?"""
    pieces_after_party = 0.5
    pieces_left_after_share = (1 - 0.5/2) * pieces_after_party
    pieces_left_after_snack = pieces_left_after_share - 1
    total_pieces = pieces_left_after_snack * 4
    result = total_pieces
    return result

print(solution())