def solution():
    """Josh has 100 feet of rope. He cuts the rope in half, and then takes one of the halves and cuts it in half again. He grabs one of the remaining pieces and cuts it into fifths. He's stuck holding one length of the rope he's most recently cut. How long is it?"""
    initial_length = 100
    first_cut_length = initial_length / 2
    second_cut_length = first_cut_length / 2
    remaining_piece_length = second_cut_length / 5
    result = remaining_piece_length
    return result

print(solution())