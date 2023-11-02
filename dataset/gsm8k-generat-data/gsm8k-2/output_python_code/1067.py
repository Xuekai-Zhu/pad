def solution():
    """Matt is playing basketball. In the first quarter, he made 2-point shots four times and 3-point shots twice. How many points did he score for that quarter?"""
    points_2pt = 2
    points_3pt = 3
    made_2pt_shots = 4
    made_3pt_shots = 2
    total_points = (points_2pt * made_2pt_shots) + (points_3pt * made_3pt_shots)
    result = total_points
    return result

print(solution())