def solution():
    """Josh has 100 feet of rope. He cuts the rope in half, and then takes one of the halves and cuts it in half again. He grabs one of the remaining pieces and cuts it into fifths. He's stuck holding one length of the rope he's most recently cut. How long is it?"""
    # Start with the original length of rope
    rope_length = 100

    # Cut the rope in half
    rope_length /= 2

    # Cut one of the halves in half again
    rope_length /= 2

    # Cut one of the remaining pieces into fifths
    rope_length /= 5
    
    result = rope_length
    return result

print(solution())