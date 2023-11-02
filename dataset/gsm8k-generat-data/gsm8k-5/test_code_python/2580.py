def solution():
    total_orange_pieces = 80 * 10  # Jillian divided each orange into 10 equal pieces
    pieces_per_friend = 4  # Each friend gets 4 pieces
    num_friends = total_orange_pieces // pieces_per_friend  # Round down to the nearest integer

    result = num_friends
    return result

print(solution())