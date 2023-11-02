def solution():
    """Donna made a cake to take to a party where the guests ate half the cake.
    The day after the party, she shared half the leftovers with her brothers.
    The following day, she ate one piece as a midnight snack. Twice as many pieces as her snack were left.
    How many pieces was the cake to begin with?"""
    
    # Calculate how many pieces were left after the party
    pieces_left_after_party = 0.5
    
    # Calculate how many pieces were left after sharing with her brothers
    pieces_left_after_sharing = pieces_left_after_party * 0.5
    
    # Calculate how many pieces Donna had as a midnight snack
    pieces_donated = 1
    
    # Calculate how many pieces were left after Donna's snack
    pieces_left_after_snack = 2 * pieces_donated
    
    # Calculate how many pieces the cake was to begin with
    total_pieces = pieces_left_after_snack + pieces_donated + pieces_left_after_sharing + pieces_left_after_party
    
    result = total_pieces
    return result

print(solution())