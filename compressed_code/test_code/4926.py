def solution():
    
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