def solution():
    starting_marbles = 100
    kept_marbles = 20
    num_friends = 5

    # Calculate the number of marbles Harold shares with his friends
    shared_marbles = starting_marbles - kept_marbles

    # Calculate how many marbles each friend gets
    marbles_per_friend = shared_marbles / num_friends
    result = marbles_per_friend
    return result

print(solution())