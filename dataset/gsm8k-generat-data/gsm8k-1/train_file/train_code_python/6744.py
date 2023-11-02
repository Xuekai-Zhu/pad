def solution():
    """There were 250 balloons in one package. Dante evenly shared the balloons among his 5 friends. Dante changed his mind and asked each of his friends to give him 11 balloons. How many balloons does each friend have now?"""
    initial_balloons = 250
    number_of_friends = 5
    shared_balloons = initial_balloons // number_of_friends
    balloons_taken_back = 11
    balloons_per_friend = shared_balloons - balloons_taken_back
    result = balloons_per_friend
    return result

print(solution())