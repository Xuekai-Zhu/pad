def solution():
    """Poppy is solving a 1000-piece jigsaw puzzle. She places a quarter of the pieces on the board, then her mom places a third of the remaining pieces. How many jigsaw pieces are left to be placed?"""
    total_pieces = 1000
    pieces_placed_by_poppy = total_pieces / 4
    pieces_remaining = total_pieces - pieces_placed_by_poppy
    pieces_placed_by_mom = pieces_remaining / 3
    pieces_left_to_place = total_pieces - (pieces_placed_by_poppy + pieces_placed_by_mom)
    result = pieces_left_to_place
    return result

print(solution())