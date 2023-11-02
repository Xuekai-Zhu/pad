def solution():
    # Calculate the total number of pieces each friend gets
    pieces_per_orange = 10  
    pieces_per_friend = 4
    total_pieces = pieces_per_orange * 80
    
    # Calculate the number of friends
    num_friends = total_pieces // pieces_per_friend
    result = num_friends
    return result

print(solution())