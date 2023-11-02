def solution():
    """Andrew bought a big bag of balloons. The bag had 303 blue balloons and 453 purple balloons. If Andrew shares half of his balloons with his brother, how many balloons does he have left?"""
    # Define the number of blue and purple balloons
    blue_balloons = 303
    purple_balloons = 453

    # Calculate the total number of balloons
    total_balloons = blue_balloons + purple_balloons

    # Calculate the number of balloons Andrew shares with his brother
    shared_balloons = total_balloons / 2

    # Calculate the number of balloons Andrew has left
    balloons_left = total_balloons - shared_balloons

    # return the result
    result = balloons_left
    return result

print(solution())