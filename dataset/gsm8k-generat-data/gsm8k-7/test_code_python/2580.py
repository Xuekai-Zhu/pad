def solution():
    num_oranges = 80
    num_pieces_per_orange = 10
    pieces_per_friend = 4

    # Calculate the total number of pieces of orange that Jillian has
    total_pieces = num_oranges * num_pieces_per_orange

    # Calculate the number of friends that Jillian has
    num_friends = total_pieces / pieces_per_friend
    result = num_friends
    return result

print(solution())