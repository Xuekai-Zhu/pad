def solution():
    """There were 672 balloons that were either green, blue, yellow, or red. They were divided into equal groups and then Anya took half of the yellow ones home. How many balloons did Anya take home?"""
    total_balloons = 672
    yellow_balloons = total_balloons / 4  # Since there are 4 colors
    groups = 2  # Half of the yellow ones
    yellow_balloons_home = (yellow_balloons / groups)
    result = yellow_balloons_home
    return result

print(solution())