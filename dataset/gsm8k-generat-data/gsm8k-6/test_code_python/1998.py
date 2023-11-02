def solution():
    # Calculate the number of marbles Harold shared with his friends
    shared_marbles = 100 - 20  # Harold kept 20 marbles
    marbles_each_friend = shared_marbles / 5  # divide the shared marbles equally among 5 friends
    result = marbles_each_friend
    return result

print(solution())