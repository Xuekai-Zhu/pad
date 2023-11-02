def solution():
    """Darcy washes and drys 20 shirts and 8 pairs of shorts. If he folds 12 of the shirts and 5 of the shorts, how many more remaining pieces of clothing does Darcy have to fold?"""
    total_shirts = 20
    total_shorts = 8
    folded_shirts = 12
    folded_shorts = 5
    remaining_shirts = total_shirts - folded_shirts
    remaining_shorts = total_shorts - folded_shorts
    remaining_pieces = remaining_shirts + remaining_shorts
    result = remaining_pieces
    return result

print(solution())