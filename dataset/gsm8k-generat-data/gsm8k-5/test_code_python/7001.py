def solution():
    total_balloons = 303 + 453  # Andrew has a total of 756 balloons
    shared_balloons = total_balloons / 2  # Andrew shares half of his balloons with his brother
    balloons_left = total_balloons - shared_balloons  # Calculate how many balloons Andrew has left
    result = balloons_left
    return result

print(solution())