def solution():
    num_balloons = 250
    num_friends = 5
    balloons_per_friend = num_balloons / num_friends

    # Subtract 11 balloons from each friend's share
    balloons_per_friend -= 11

    result = balloons_per_friend
    return result

print(solution())