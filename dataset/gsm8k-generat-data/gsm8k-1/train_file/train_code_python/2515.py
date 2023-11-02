def solution():
    """Kate has 2 red balloons and 4 blue balloons. Assuming she inflates 4 more balloons, two of each color red and blue, what is the percent likelihood that one selected at random will be red?"""
    total_red_balloons = 2 + 2
    total_balloons = 2 + 4 + 4
    probability_red = (total_red_balloons / total_balloons) * 100
    result = probability_red
    return result

print(solution())