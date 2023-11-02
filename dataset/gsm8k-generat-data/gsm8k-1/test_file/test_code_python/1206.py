def solution():
    """To kick off summer, Jolene is having a water balloon fight with her friends. They fill up 10 packs of balloons that have 30 balloons per pack. By the end of the afternoon, 12 balloons are left. How many balloons did they throw?"""
    packs_of_balloons = 10
    balloons_per_pack = 30
    total_balloons = packs_of_balloons * balloons_per_pack
    balloons_thrown = total_balloons - 12
    result = balloons_thrown
    return result

print(solution())