def solution():
    # Calculate the total number of balloons
    total_balloons = 303 + 453

    # Calculate the number of balloons Andrew shares
    shared_balloons = total_balloons / 2

    # Calculate the number of balloons Andrew has left
    balloons_left = total_balloons - shared_balloons
    result = balloons_left
    return result

print(solution())