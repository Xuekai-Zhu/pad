def solution():
    """Jillian had 80 oranges which she had bought to give to her friends. She divided each orange into ten equal pieces for each friend to get four pieces. How many friends were there?"""
    # Define the total number of oranges and the number of pieces per orange
    total_oranges = 80
    pieces_per_orange = 10

    # Calculate the total number of pieces
    total_pieces = total_oranges * pieces_per_orange

    # Calculate the number of friends that can receive four pieces each
    num_friends = total_pieces // 4

    # return the result
    result = num_friends
    return result

print(solution())