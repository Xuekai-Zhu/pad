def solution():
    
    starting_marbles = 100
    kept_marbles = 20
    remaining_marbles = starting_marbles - kept_marbles
    num_friends = 5
    marbles_per_friend = remaining_marbles / num_friends
    result = marbles_per_friend
    return result

print(solution())