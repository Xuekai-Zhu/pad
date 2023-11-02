def solution():
    """Josh has 100 feet of rope.  He cuts the rope in half, and then takes one of the halves and cuts it in half again.  He grabs one of the remaining pieces and cuts it into fifths.  He's stuck holding one length of the rope he's most recently cut.  How long is it?"""
    # Cut the rope in half
    half_rope = 100 / 2

    # Cut one of the halves in half again
    quarter_rope = half_rope / 2

    # Cut one of the remaining pieces into fifths
    fifth_rope = quarter_rope / 5

    # The length of the rope Josh is holding is the length of the fifth piece
    result = fifth_rope
    return result

print(solution())