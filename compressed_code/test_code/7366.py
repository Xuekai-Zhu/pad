def solution():
    
    starting_marbles = 100
    kept_marbles = 20
    shared_marbles = starting_marbles - kept_marbles
    friends = 5
    marbles_per_friend = shared_marbles / friends
    result = marbles_per_friend
    return result

print(solution())