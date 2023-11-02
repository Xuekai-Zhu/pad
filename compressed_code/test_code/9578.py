def solution():
    
    total_pieces = 11
    lyndee_pieces = 1
    friend_pieces = 2
    remaining_pieces = total_pieces - lyndee_pieces
    num_friends = remaining_pieces // friend_pieces
    result = num_friends
    return result

print(solution())