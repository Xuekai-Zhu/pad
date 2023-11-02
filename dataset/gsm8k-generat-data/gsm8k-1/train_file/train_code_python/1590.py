def solution():
    """There are 3414 yellow balloons and there are 1762 more black balloons than yellow balloons. If the balloons will be evenly divided among 10 schools, how many balloons will one school receive?"""
    yellow_balloons = 3414
    black_balloons = yellow_balloons + 1762
    total_balloons = yellow_balloons + black_balloons
    balloons_per_school = total_balloons / 10
    result = balloons_per_school
    return result

print(solution())