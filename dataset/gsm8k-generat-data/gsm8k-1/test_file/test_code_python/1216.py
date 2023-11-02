def solution():
    """Ian has a board that is 40 feet long. He decides to make a cut so he can have two pieces. The longer piece is 4 times longer than the shorter piece. How long is the longer piece?"""
    total_length = 40
    shorter_piece = total_length / 5
    longer_piece = 4 * shorter_piece
    result = longer_piece
    return result

print(solution())