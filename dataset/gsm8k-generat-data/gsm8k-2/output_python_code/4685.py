def solution():
    """Darcy washes and dries 20 shirts and 8 pairs of shorts. If he folds 12 of the shirts and 5 of the shorts, how many more remaining pieces of clothing does Darcy have to fold?"""
    total_shirts = 20
    total_shorts = 8 * 2
    folded_shirts = 12
    folded_shorts = 5 * 2
    remaining_shirts = total_shirts - folded_shirts
    remaining_shorts = total_shorts - folded_shorts
    total_remaining = remaining_shirts + remaining_shorts
    result = total_remaining
    return result

print(solution())