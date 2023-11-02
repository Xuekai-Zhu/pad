def solution():
    """A high school bowling team's 3 members scored a total of 810 points in their first match. The first bowler scored 1/3 as many points as the second, and the second bowler scored 3 times as high as the third bowler. How many points did the third bowler score?"""
    total_points = 810
    second_bowler_points = x
    first_bowler_points = second_bowler_points / 3
    third_bowler_points = second_bowler_points / 9
    if first_bowler_points + second_bowler_points + third_bowler_points == total_points:
        result = third_bowler_points
    return result

print(solution())