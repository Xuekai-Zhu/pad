def solution():
    """Parker chews 4 pieces of gum a day. A pack of gum has 15 pieces of chewing gum per pack. How many packs of gum will he need to last him 30 days?"""
    pieces_per_day = 4
    pieces_per_pack = 15
    days = 30
    total_pieces = pieces_per_day * days
    packs = total_pieces // pieces_per_pack + 1
    result = packs
    return result

print(solution())