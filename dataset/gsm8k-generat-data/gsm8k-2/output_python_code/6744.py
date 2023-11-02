def solution():
    """There were 250 balloons in one package. Dante evenly shared the balloons among his 5 friends. Dante changed his mind and asked each of his friends to give him 11 balloons. How many balloons does each friend have now?"""
    total_balloons = 250
    num_friends = 5
    balloons_per_friend = total_balloons / num_friends
    balloons_per_friend -= 11
    result = balloons_per_friend
    return result

print(solution())