def solution():
    """Jillian had 80 oranges which she had bought to give to her friends. She divided each orange into ten equal pieces for each friend to get four pieces. How many friends were there?"""
    oranges = 80
    pieces_per_orange = 10
    pieces_per_friend = 4
    friends = (oranges * pieces_per_orange) // pieces_per_friend
    result = friends
    return result

print(solution())