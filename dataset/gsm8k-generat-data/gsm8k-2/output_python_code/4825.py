def solution():
    """Tyson played basketball on the schoolyard. He scored three points fifteen times, and two points twelve times. He also scored one point some number of times. How many times did he score one point, if in total he scored 75 points?"""
    total_points = 75
    three_points = 15 * 3
    two_points = 12 * 2
    one_points = total_points - three_points - two_points
    result = one_points
    return result

print(solution())