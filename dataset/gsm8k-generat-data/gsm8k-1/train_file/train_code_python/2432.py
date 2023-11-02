def solution():
    """Josh has 100 feet of rope. He cuts the rope in half, and then takes one of the halves and cuts it in half again. He grabs one of the remaining pieces and cuts it into fifths. He's stuck holding one length of the rope he's most recently cut. How long is it?"""
    rope_length = 100
    rope_half = rope_length / 2
    rope_quarter = rope_half / 2
    rope_fifth = rope_quarter / 5
    result = rope_fifth
    return result

print(solution())