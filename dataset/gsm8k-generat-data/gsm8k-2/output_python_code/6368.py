def solution():
    """A rope has a length of 200 meters. Stefan cuts the rope into four equal parts, gives his mother half of the cut pieces, and subdivides the remaining pieces into two more equal parts. What's the length of each piece?"""
    rope_length = 200
    num_pieces = 4
    cut_length = rope_length / num_pieces
    mother_length = cut_length * 2
    remaining_pieces = num_pieces - 2
    subdivided_length = cut_length / 2
    final_length = subdivided_length
    result = final_length
    return result

print(solution())