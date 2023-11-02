def solution():
    # Calculate the total number of balloons in the bag
    total_balloons = 303 + 453

    # Calculate the number of balloons Andrew shares with his brother
    shared_balloons = total_balloons / 2

    # Calculate the number of balloons left with Andrew
    balloons_left = total_balloons - shared_balloons

    result = balloons_left
    return result

print(solution())