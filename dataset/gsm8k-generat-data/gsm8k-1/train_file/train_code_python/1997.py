def solution():
    """Harold had 100 marbles. He kept 20 marbles and shared the rest evenly among his 5 friends. How many marbles did each friend get?"""
    starting_marbles = 100
    kept_marbles = 20
    shared_marbles = starting_marbles - kept_marbles
    friends = 5
    marbles_per_friend = shared_marbles / friends
    result = marbles_per_friend
    return result

print(solution())