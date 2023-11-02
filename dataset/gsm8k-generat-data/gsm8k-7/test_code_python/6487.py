def solution():
    num_friends = 3
    marbles_per_friend = 20
    marbles_left = 5

    # Calculate the total number of marbles given to friends
    total_marbles_given = num_friends * marbles_per_friend

    # Calculate the total number of marbles Zack initially had
    initial_num_marbles = total_marbles_given + marbles_left
    result = initial_num_marbles
    return result

print(solution())