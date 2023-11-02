def solution():
    """Jillian had 80 oranges which she had bought to give to her friends. She divided each orange into ten equal pieces for each friend to get four pieces. How many friends were there?"""
    # Define the total number of orange pieces
    total_pieces = 80 * 10

    # Calculate the number of friends
    num_friends = total_pieces // 4

    # Display the number of friends
    result = num_friends
    return result

print(solution())