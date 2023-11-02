def solution():
    """Bess and Holly are playing Frisbee at the park. Bess can throw the Frisbee as far as 20 meters and she does this 4 times. Holly can only throw the Frisbee as far as 8 meters and she does this 5 times. Each time Bess throws a Frisbee, she throws it back to her original position. Holly leaves her Frisbee where it lands every time she throws it. In total, how many meters have the thrown Frisbees traveled?"""
    bess_distance = 20 * 4 * 2 # 2 is for throwing and returning
    holly_distance = 8 * 5 # she does not throw it back
    total_distance = bess_distance + holly_distance
    result = total_distance
    return result

print(solution())