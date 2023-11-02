def solution():
    """Mrs. Crocker made 11 pieces of fried chicken for Lyndee and her friends. If Lyndee only ate one piece but each of her friends got to eat 2 pieces, how many friends did Lyndee have over?"""
    total_pieces = 11
    lyndee_pieces = 1
    friend_pieces = 2
    remaining_pieces = total_pieces - lyndee_pieces
    num_friends = remaining_pieces // friend_pieces
    result = num_friends
    return result

print(solution())