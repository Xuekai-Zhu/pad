def solution():
    """There were 672 balloons that were either green, blue, yellow, or red. They were divided into equal groups and then Anya took half of the yellow ones home. How many balloons did Anya take home?"""
    total_balloons = 672
    groups = 4 # since there are 4 colors of balloons
    balloons_per_group = total_balloons / groups
    yellow_balloons = balloons_per_group # since they are divided equally
    balloons_taken = yellow_balloons / 2
    result = balloons_taken
    return result

print(solution())