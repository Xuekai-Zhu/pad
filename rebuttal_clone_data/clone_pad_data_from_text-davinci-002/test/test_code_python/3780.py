def solution():
    initial_balloons = 250
    friends = 5
    balloons_given = 11

    balloons_received = (friends - 1) * balloons_given
    balloons_left = initial_balloons - (friends * balloons_given)
    balloons_per_friend = balloons_left / friends

    result = balloons_per_friend
    return result

print(solution())