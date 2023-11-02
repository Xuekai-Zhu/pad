def solution():
    """Jillian had 80 oranges which she had bought to give to her friends. She divided each orange into ten equal pieces for each friend to get four pieces. How many friends were there?"""
    total_pieces = 80 * 10
    pieces_per_friend = 4
    total_friends = total_pieces // pieces_per_friend
    result = total_friends
    return result

print(solution())