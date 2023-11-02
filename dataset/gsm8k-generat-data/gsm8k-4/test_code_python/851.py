def solution():
    """In a card game, you are awarded 10 points if you win one round. While playing, Jane ends up with 60 points. If she lost 20 points, then how many rounds did she play?"""
    # Define the points awarded for winning a round
    POINTS_PER_ROUND = 10

    # Define the initial number of rounds
    rounds = 0

    # Calculate the number of rounds won based on the total points and points lost
    rounds = (60 - 20) / POINTS_PER_ROUND

    # Return the result
    result = rounds
    return result

print(solution())