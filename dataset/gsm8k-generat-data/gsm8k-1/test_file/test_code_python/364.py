def solution():
    """After scoring 14 points, Erin now has three times more points than Sara, who scored 8. How many points did Erin have before?"""
    sara_score = 8
    erin_score = 14
    erin_ratio = 3
    sara_ratio = 1
    sara_multiplier = erin_ratio + sara_ratio
    erin_multiplier = sara_multiplier * 3
    sara_points = sara_score * sara_multiplier
    erin_points = erin_score * erin_multiplier - sara_points
    result = erin_points
    
    return result

print(solution())