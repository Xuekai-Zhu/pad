def solution():
    
    total_balloons = 250
    num_friends = 5
    balloons_per_friend = total_balloons / num_friends
    balloons_per_friend -= 11
    result = balloons_per_friend
    return result

print(solution())