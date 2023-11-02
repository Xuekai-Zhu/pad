def solution():
    # Define the length of the rope
    rope_length = 200

    # Divide the rope into four equal parts
    equal_parts = rope_length / 4

    # Give half of the cut pieces to Stefan's mother
    mother_parts = equal_parts * 2

    # Divide the remaining pieces into two equal parts
    remaining_parts = equal_parts * 2
    final_parts = remaining_parts / 2

    # Calculate the length of each piece
    piece_length = final_parts

    result = piece_length
    return result

print(solution())