def solution():
    starting_marbles = 100  # Harold had 100 marbles
    kept_marbles = 20  # Harold kept 20 marbles
    shared_marbles = starting_marbles - kept_marbles  # Harold shared the rest of the marbles
    friends = 5  # Harold shared the marbles with 5 friends

    # Calculate how many marbles each friend received
    marbles_per_friend = shared_marbles // friends
    result = marbles_per_friend
    return result

print(solution())